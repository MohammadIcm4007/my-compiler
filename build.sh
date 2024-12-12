rm -rf ./build
g++ my-compiler.cpp -o my-compiler
mkdir build
mv my-compiler ./build
cp nasm ./build
cp ld ./build
