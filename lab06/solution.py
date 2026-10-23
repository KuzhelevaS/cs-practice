import pathlib

def count_by_extension(paths: list[str]) -> dict[str, int]:
    result = dict()
    for el in paths:
        suffix = pathlib.Path(el).suffix.lower()
        if len(suffix) > 1:
            suffix = suffix[1:]
        result[suffix] = result.get(suffix, 0) + 1
    return result

def deepest_path(paths: list[str]) -> str:
    result = pathlib.Path("")
    saved = ""
    for el in paths:
        path = pathlib.Path(el)
        if len(path.parts) > len(result.parts):
            result = path
            saved = el
        elif len(result.parts) == len(path.parts) and el < saved:
            result = path
            saved = el
    return saved

def test():
    paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]

    assert count_by_extension(paths) == {"pdf": 1, "txt": 1, "png": 1, "": 1}
    assert count_by_extension([]) == {}
    assert count_by_extension(["a.tar.gz", ".gitignore"]) == {"gz": 1, "": 1}

    assert deepest_path(paths) == "docs/img/logo.png"
    assert deepest_path(["a/b/c.txt", "x/y/z.txt"]) == "a/b/c.txt"
    assert deepest_path(["x/y/z.txt", "a/b/c.txt"]) == "a/b/c.txt"
    assert deepest_path([]) == ""

    #assert human_size(900) == "900 Б"
    #assert human_size(1536) == "1.5 КБ"
    #assert human_size(5 * 1024 * 1024) == "5.0 МБ"

if __name__ == "__main__":
    test()