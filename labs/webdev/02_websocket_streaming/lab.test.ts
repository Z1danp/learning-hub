import { test } from 'node:test';
import assert from 'node:assert';
import { solveChallenge } from './lab.ts';

test('starter test', () => {
  assert.strictEqual(typeof solveChallenge, 'function');
});
