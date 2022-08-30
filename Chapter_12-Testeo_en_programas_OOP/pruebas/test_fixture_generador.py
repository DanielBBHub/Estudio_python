import pytest
import tempfile
import shutil
import os.path

@pytest.fixture
def dir_temporal(request):
    dir = tempfile.mkdtemp()
    print(dir)
    yield dir
    shutil.rmtree(dir)

def test_archivos_os(dir_temporal):
    os.mkdir(os.path.join(dir_temporal,"a"))
    os.mkdir(os.path.join(dir_temporal,"b"))
    contenidos_dir = os.listdir(dir_temporal)
    print(contenidos_dir)
    assert len(contenidos_dir) == 2
    assert "a" in contenidos_dir
    assert "b" in contenidos_dir