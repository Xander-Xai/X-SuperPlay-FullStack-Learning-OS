/** Demand-first JS race lab: pure Node unit tests, NOT a Vue/React integration test. */
import test from 'node:test';
import assert from 'node:assert/strict';

function deferred() {
  let resolve, reject;
  const promise = new Promise((ok, bad) => {
    resolve = ok;
    reject = bad;
  });
  return { promise, resolve, reject };
}

function naiveSearch() {
  return {
    result: null,
    async search(promise) {
      this.result = await promise;
    },
  };
}

function versionedSearch() {
  let sequence = 0;
  return {
    result: null,
    error: null,
    async search(promise) {
      const current = ++sequence;
      try {
        const next = await promise;
        if (current === sequence) {
          this.result = next;
          this.error = null;
        }
      } catch (error) {
        if (current === sequence) this.error = error.message;
      }
    },
  };
}

test('failure reproduction: naive search lets old response overwrite new', async () => {
  const a = deferred();
  const b = deferred();
  const ui = naiveSearch();
  const first = ui.search(a.promise);
  const second = ui.search(b.promise);
  b.resolve('query-B-new');
  await second;
  a.resolve('query-A-old');
  await first;
  assert.equal(ui.result, 'query-A-old'); // Reproduces a BUG; this is not the desired behavior.
});

test('fixed: request generation ignores obsolete completion', async () => {
  const a = deferred();
  const b = deferred();
  const ui = versionedSearch();
  const first = ui.search(a.promise);
  const second = ui.search(b.promise);
  b.resolve('query-B-new');
  await second;
  a.resolve('query-A-old');
  await first;
  assert.equal(ui.result, 'query-B-new');
  assert.equal(ui.error, null);
});

test('fixed: stale rejection does not replace newer success with error', async () => {
  const a = deferred();
  const b = deferred();
  const ui = versionedSearch();
  const first = ui.search(a.promise);
  const second = ui.search(b.promise);
  b.resolve('query-B-new');
  await second;
  a.reject(new Error('old request failed'));
  await first;
  assert.equal(ui.result, 'query-B-new');
  assert.equal(ui.error, null);
});
