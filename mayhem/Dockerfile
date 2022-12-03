FROM fuzzers/atheris:2.0.7-python3.9

# Build
RUN pip install kivy[base]

ADD ./mayhem/fuzz_load_string.py /fuzz_load_string.py

CMD ["/fuzz_load_string.py"]
