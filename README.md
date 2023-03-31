# Aleo setup

In order to get started with lookup tables in Aleo instructions, you can:

```
git submodule update --init --recursive
mkdir -p ~/.aleo/resources/
pip3 install gdown
python3 get_aleo_resources.py
cp aleo_lookup_resources/* ~/.aleo/resources/
cd aleo && cargo build
```

Testing an Aleo file:
```
cd aleo/examples/simple_token
../../target/debug/aleo run mint aleo1vrxcf2y4hc230wax2urapkcr0ws2zmkz40vpwgd6fstsggk97q9sd6lszx 1u64
```
