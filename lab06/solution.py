import pathlib
import pathlib as p

def count_by_extension(paths: list[str]) -> dict[str, int]:
    result = dict()
    for el in paths:
        suffix = pathlib.Path(el).suffix.lower()
        if len(suffix) > 1:
            suffix = suffix[1:]
        result[suffix] = result.get(suffix, 0) + 1
    return result

def test():
    paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]

    assert count_by_extension(paths) == {"pdf": 1, "txt": 1, "png": 1, "": 1}
    assert count_by_extension([]) == {}
    assert count_by_extension(["a.tar.gz", ".gitignore"]) == {"gz": 1, "": 1}

    #assert deepest_path(paths) == "docs/img/logo.png"

    #assert human_size(900) == "900 Б"
    #assert human_size(1536) == "1.5 КБ"
    #assert human_size(5 * 1024 * 1024) == "5.0 МБ"

if __name__ == "__main__":
    test()