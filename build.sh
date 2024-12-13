rm -rf ./build
g++ my-lang.cpp -o my-lang
mkdir build
mv my-lang ./build
cp nasm ./build
cp ld ./build
