import * as fs from 'fs'
import * as path from 'path'

const inputPath = path.join(__dirname, 'input.txt')
const input: string[] = fs.readFileSync(inputPath, 'utf-8').trim().split('\n')

const LOCK_SIZE = 100

function countZeroCrossings(
  startPos: number,
  amount: number,
  direction: number
): number {
  if (amount === 0) return 0

  const firstZeroStep =
    direction === 1
      ? startPos === 0
        ? LOCK_SIZE
        : LOCK_SIZE - startPos
      : startPos === 0
        ? LOCK_SIZE
        : startPos

  if (amount < firstZeroStep) return 0
  return Math.floor((amount - firstZeroStep) / LOCK_SIZE) + 1
}

function main() {
  const fin = input
    .map((line) => ({
      direction: line[0] === 'L' ? -1 : 1,
      amount: parseInt(line.substring(1).trim()),
    }))
    .reduce(
      (agg, x) => {
        let current = (agg.current + x.direction * x.amount) % LOCK_SIZE
        if (current < 0) {
          current = LOCK_SIZE + current
        }

        const zeroCrossings = countZeroCrossings(
          agg.current,
          x.amount,
          x.direction
        )
        const numZeroes = agg.numZeroes + zeroCrossings

        console.log(
          `Move ${x.direction * x.amount}: from ${agg.current} to ${current}, crossings: ${zeroCrossings}, total zeroes: ${numZeroes}`
        )

        return {
          current,
          numZeroes,
        }
      },
      { current: 50, numZeroes: 0 }
    )

  console.log(fin)
}

main()
