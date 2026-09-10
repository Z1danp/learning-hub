/**
 * Lab 01: Building an Async Concurrency Task Queue
 * Domain: Modern Web Development / Asynchronous Systems
 *
 * Problem Challenge:
 * Bangun antrean tugas asinkron (Task Queue) dengan batas konkurensi (limit).
 * Jika ada 10 tugas yang masuk tapi limit=2, maka hanya maksimal 2 tugas yang boleh
 * berjalan bersamaan. Begitu salah satu tugas selesai, tugas berikutnya di antrean langsung dieksekusi.
 */

export type AsyncTask<T> = () => Promise<T>;

export class ConcurrencyQueue {
  private limit: number;
  private running = 0;
  private queue: Array<{ task: AsyncTask<any>; resolve: (v: any) => void; reject: (e: any) => void }> = [];

  constructor(limit: number) {
    this.limit = limit;
  }

  async add<T>(task: AsyncTask<T>): Promise<T> {
    return new Promise<T>((resolve, reject) => {
      this.queue.push({ task, resolve, reject });
      this.processNext();
    });
  }

  private async processNext(): Promise<void> {
    if (this.running >= this.limit || this.queue.length === 0) {
      return;
    }

    const item = this.queue.shift();
    if (!item) return;

    this.running++;

    try {
      const result = await item.task();
      item.resolve(result);
    } catch (err) {
      item.reject(err);
    } finally {
      this.running--;
      this.processNext();
    }
  }

  get activeCount(): number {
    return this.running;
  }

  get pendingCount(): number {
    return this.queue.length;
  }
}
