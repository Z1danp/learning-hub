import { test } from 'node:test';
import assert from 'node:assert';
import { ConcurrencyQueue } from './lab.ts';

test('ConcurrencyQueue limits concurrent executions to max limit', async () => {
  const queue = new ConcurrencyQueue(2);
  let maxConcurrent = 0;
  let currentlyRunning = 0;

  const makeTask = (delayMs: number, id: number) => async () => {
    currentlyRunning++;
    if (currentlyRunning > maxConcurrent) {
      maxConcurrent = currentlyRunning;
    }
    await new Promise((res) => setTimeout(res, delayMs));
    currentlyRunning--;
    return id;
  };

  const results = await Promise.all([
    queue.add(makeTask(50, 1)),
    queue.add(makeTask(50, 2)),
    queue.add(makeTask(50, 3)),
    queue.add(makeTask(50, 4)),
  ]);

  assert.deepStrictEqual(results, [1, 2, 3, 4]);
  assert.strictEqual(maxConcurrent, 2, 'Max concurrent executions should not exceed limit of 2');
  assert.strictEqual(queue.activeCount, 0);
  assert.strictEqual(queue.pendingCount, 0);
});
