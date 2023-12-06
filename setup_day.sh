echo "Creating folder day$1"
echo "- **Day $1**" >> README.md
echo "  - :x: [Python](./day$1/python/)" >> README.md
echo "  - :x: [Rust](./day$1/rust/)" >> README.md
code .
mkdir day$1
cd day$1
mkdir python
cp ../python_template.py ./python/main.py
touch input.txt
cargo new rust
cd python
