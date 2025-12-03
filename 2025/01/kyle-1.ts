import * as fs from 'fs'
import * as path from 'path'

const inputPath = path.join(__dirname, 'input.txt')
const input: string[] = fs.readFileSync(inputPath, 'utf-8').trim().split('\n')

const LOCK_SIZE = 100

function main() {
  const fin = input
    .map((line) => ({
      direction: line[0] == 'L' ? 1 : -1,
      amount: line.substring(1).trim(),
    }))
    .reduce(
      (agg, x) => {
        const amount = parseInt(x.amount)
        const current =
          (agg.current + ((x.direction * amount) % LOCK_SIZE) + LOCK_SIZE) %
          LOCK_SIZE

        const numZeroes = agg.numZeroes + (current == 0 ? 1 : 0)

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
