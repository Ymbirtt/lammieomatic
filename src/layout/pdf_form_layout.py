from base_layout import BaseLayout
from fdfgen import forge_fdf
from subprocess import call
from tempfile import NamedTemporaryFile, tempdir
from os import path

class PdfFormLayout(BaseLayout):
    form_file = NotImplemented

    @classmethod
    def render(cls, items, output_path):
        chunk_size = cls.max_items
        fdfs = []
        for i in range(0, len(items), chunk_size):
            chunk = items[i:i+chunk_size]
            fdf = cls.__generate_fdf(chunk)
            fdfs.append(fdf)
        return cls.__render_forms(fdfs, output_path)

    @classmethod
    def __generate_fdf(cls, chunk):
        attrs = []
        for (i, item) in enumerate(chunk):
            attrs += cls._item_to_attrs(i, item).items()
        return forge_fdf(fdf_data_strings=attrs)

    @classmethod
    def _item_to_attrs(cls, index, item):
        raise NotImplementedError

    @classmethod
    def __render_forms(cls, fdfs, output_path):
        pdf_files = []
        for i, fdf in enumerate(fdfs):
            fdf_file = NamedTemporaryFile('w+b', suffix='.fdf', delete=False)
            fdf_file.write(fdf)
            fdf_file.close()
            print "Calling pdftk fill_form"
            print fdf_file.name
            pdf_files.append('output{0}.pdf'.format(i))
            call(['pdftk', cls.form_file, 'fill_form', fdf_file.name, 'output', path.join('output{0}.pdf'.format(i)), 'flatten'])
        print "Calling pdftk cat"
        call(['pdftk'] + pdf_files + ['cat', 'output', output_path])
