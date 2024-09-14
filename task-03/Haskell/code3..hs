```haskell
import Control.Monad (replicateM_)

printDiamond :: Int -> IO ()
printDiamond n = do
    replicateM_ n $ \i -> do
        putStrLn $ replicate (n - i - 1) ' ' ++ replicate (2 * i + 1) '*'
    replicateM_ (n - 2) $ \i -> do
        putStrLn $ replicate (n - i - 1) ' ' ++ replicate (2 * i + 1) '*'

main :: IO ()
main = do
    putStr "Enter a number: "
    n <- readLn
    printDiamond n
```
