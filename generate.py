from args import prepare_args
from text_generator import TextGenerator


if __name__ == "__main__":
    args = prepare_args({
        "model": "Enter model: ",
        "length": "Enter length: ",
        "prefix": None
    })
    generator = TextGenerator()
    generator.restore(args["model"])
    text = generator.generate(int(args["length"]), args["prefix"])
    print(text)
