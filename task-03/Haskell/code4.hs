import System.IO

printDiamond :: Int -> String
printDiamond n = unlines (upperHalf ++ lowerHalf)
  where
    upperHalf = [replicate (n - i - 1) ' ' ++ replicate (2 * i + 1) '*' | i <- [0..n-1]]
    lowerHalf = [replicate (n - i - 1) ' ' ++ replicate (2 * i + 1) '*' | i <- reverse [0..(n-2)]]

main :: IO ()
main = do
    content <- readFile "input.txt"
    let n = read (init content) :: Int
    let diamond = printDiamond n
    writeFile "output.txt" diamond