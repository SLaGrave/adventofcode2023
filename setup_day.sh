echo "Creating folder day$1"
mkdir day$1
cd day$1
mkdir python
cp ../python_template.py ./python/main.py
touch input.txt
cargo new rust
cd ..
