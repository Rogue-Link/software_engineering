import difflib
import PyQt5

class DiffFile:

    @classmethod
    def _read_file(cls, file):
        try:
            with open(file, "rb") as fp:
                lines = fp.read().decode('utf-8')
                text = lines.splitlines()
                return text
        except Exception as e:
            print("ERROR: %s" % str(e))

    @classmethod
    def compare_file(cls, file1, file2, out_file):
        file1_content = cls._read_file(file1)
        file2_content = cls._read_file(file2)
        compare = difflib.HtmlDiff()
        compare_result = compare.make_file(file1_content, file2_content)
        with open(out_file, 'w') as fp:
            fp.writelines(compare_result)

    @classmethod
    def compare_text(cls, src_text, target_text):
        d = difflib.Differ()
        return "".join(list(d.compare(src_text, target_text)))

    @classmethod
    def compare_text_to_file(cls, src_text, target_text, out_file):
        compare = difflib.HtmlDiff()
        compare_result = compare.make_file(src_text, target_text)
        with open(out_file, 'w') as fp:
            fp.writelines(compare_result)
