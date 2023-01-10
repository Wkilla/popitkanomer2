import unittest
import Model

class TestModel(unittest.TestCase):
    

    def test_updateAlbums(self):
        self._model = Model.Model()
        self._model.updateAlbums(8, "Divisive")
        test = self._model.getAlbumsSQL()
        self.assertIn(['Divisive', 8], test)



if __name__ == '__main__':
    unittest.main()