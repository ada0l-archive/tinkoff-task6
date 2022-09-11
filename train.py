from args import prepare_args
from text_generator import TextGenerator


if __name__ == "__main__":
    args = prepare_args({
        "input-dir": "Enter input dir: ",
        "model": "Enter model: "
    })
    generator = TextGenerator()
    generator.fit(args["input-dir"], args["model"])
