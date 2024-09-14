import System.IO

main :: IO ()
main = do
    -- Read from input.txt and write to output.txt
    content <- readFile "input.txt"
    writeFile "output.txt" content
