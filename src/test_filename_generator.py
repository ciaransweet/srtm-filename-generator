import unittest

import filename_generator


class Tests(unittest.TestCase):

    def test_north_east(self):
        btm_lat = 1.5
        top_lat = 3.5
        left_lon = 1.5
        right_lon = 3.5
        expected_filenames = ['N01E001.SRTMGL1.hgt.zip', 'N01E002.SRTMGL1.hgt.zip', 'N01E003.SRTMGL1.hgt.zip',
                              'N02E001.SRTMGL1.hgt.zip', 'N02E002.SRTMGL1.hgt.zip', 'N02E003.SRTMGL1.hgt.zip',
                              'N03E001.SRTMGL1.hgt.zip', 'N03E002.SRTMGL1.hgt.zip', 'N03E003.SRTMGL1.hgt.zip']
        filenames = filename_generator.generate_filenames(btm_lat, top_lat, left_lon, right_lon)
        self.assertListEqual(filenames, expected_filenames)

    def test_north_west(self):
        btm_lat = 1.5
        top_lat = 3.5
        left_lon = -2.5
        right_lon = -0.5
        expected_filenames = ['N01W003.SRTMGL1.hgt.zip', 'N01W002.SRTMGL1.hgt.zip', 'N01W001.SRTMGL1.hgt.zip',
                              'N02W003.SRTMGL1.hgt.zip', 'N02W002.SRTMGL1.hgt.zip', 'N02W001.SRTMGL1.hgt.zip',
                              'N03W003.SRTMGL1.hgt.zip', 'N03W002.SRTMGL1.hgt.zip', 'N03W001.SRTMGL1.hgt.zip']
        filenames = filename_generator.generate_filenames(btm_lat, top_lat, left_lon, right_lon)
        self.assertListEqual(filenames, expected_filenames)

    def test_south_west(self):
        btm_lat = -10.5
        top_lat = -7.5
        left_lon = -120.5
        right_lon = -117.5
        expected_filenames = ['S11W121.SRTMGL1.hgt.zip', 'S11W120.SRTMGL1.hgt.zip', 'S11W119.SRTMGL1.hgt.zip',
                              'S11W118.SRTMGL1.hgt.zip',
                              'S10W121.SRTMGL1.hgt.zip', 'S10W120.SRTMGL1.hgt.zip', 'S10W119.SRTMGL1.hgt.zip',
                              'S10W118.SRTMGL1.hgt.zip',
                              'S09W121.SRTMGL1.hgt.zip', 'S09W120.SRTMGL1.hgt.zip', 'S09W119.SRTMGL1.hgt.zip',
                              'S09W118.SRTMGL1.hgt.zip',
                              'S08W121.SRTMGL1.hgt.zip', 'S08W120.SRTMGL1.hgt.zip', 'S08W119.SRTMGL1.hgt.zip',
                              'S08W118.SRTMGL1.hgt.zip']
        filenames = filename_generator.generate_filenames(btm_lat, top_lat, left_lon, right_lon)
        self.assertListEqual(filenames, expected_filenames)

    def test_south_east(self):
        btm_lat = -10.5
        top_lat = -7.5
        left_lon = 117.5
        right_long = 120.5
        expected_filenames = ['S11E117.SRTMGL1.hgt.zip', 'S11E118.SRTMGL1.hgt.zip', 'S11E119.SRTMGL1.hgt.zip',
                              'S11E120.SRTMGL1.hgt.zip',
                              'S10E117.SRTMGL1.hgt.zip', 'S10E118.SRTMGL1.hgt.zip', 'S10E119.SRTMGL1.hgt.zip',
                              'S10E120.SRTMGL1.hgt.zip',
                              'S09E117.SRTMGL1.hgt.zip', 'S09E118.SRTMGL1.hgt.zip', 'S09E119.SRTMGL1.hgt.zip',
                              'S09E120.SRTMGL1.hgt.zip',
                              'S08E117.SRTMGL1.hgt.zip', 'S08E118.SRTMGL1.hgt.zip', 'S08E119.SRTMGL1.hgt.zip',
                              'S08E120.SRTMGL1.hgt.zip']
        filenames = filename_generator.generate_filenames(btm_lat, top_lat, left_lon, right_long)
        self.assertListEqual(filenames, expected_filenames)

    def test_equator_cross_east(self):
        btm_lat = -1.5
        top_lat = 1.5
        left_lon = 1.5
        right_lon = 3.5
        expected_filenames = ['S02E001.SRTMGL1.hgt.zip', 'S02E002.SRTMGL1.hgt.zip', 'S02E003.SRTMGL1.hgt.zip',
                              'S01E001.SRTMGL1.hgt.zip', 'S01E002.SRTMGL1.hgt.zip', 'S01E003.SRTMGL1.hgt.zip',
                              'N00E001.SRTMGL1.hgt.zip', 'N00E002.SRTMGL1.hgt.zip', 'N00E003.SRTMGL1.hgt.zip',
                              'N01E001.SRTMGL1.hgt.zip', 'N01E002.SRTMGL1.hgt.zip', 'N01E003.SRTMGL1.hgt.zip']
        filenames = filename_generator.generate_filenames(btm_lat, top_lat, left_lon, right_lon)
        self.assertListEqual(filenames, expected_filenames)

    def test_equator_cross_west(self):
        btm_lat = -1.5
        top_lat = 1.5
        left_lon = -3.5
        right_lon = -1.5
        expected_filenames = ['S02W004.SRTMGL1.hgt.zip', 'S02W003.SRTMGL1.hgt.zip', 'S02W002.SRTMGL1.hgt.zip',
                              'S01W004.SRTMGL1.hgt.zip', 'S01W003.SRTMGL1.hgt.zip', 'S01W002.SRTMGL1.hgt.zip',
                              'N00W004.SRTMGL1.hgt.zip', 'N00W003.SRTMGL1.hgt.zip', 'N00W002.SRTMGL1.hgt.zip',
                              'N01W004.SRTMGL1.hgt.zip', 'N01W003.SRTMGL1.hgt.zip', 'N01W002.SRTMGL1.hgt.zip']
        filenames = filename_generator.generate_filenames(btm_lat, top_lat, left_lon, right_lon)
        self.assertListEqual(filenames, expected_filenames)

    def test_international_dateline_all_quadrants(self):
        btm_lat = -2.5
        top_lat = 1.5
        left_lon = 177.5
        right_lon = -178.5
        expected_filenames = ['S03E177.SRTMGL1.hgt.zip', 'S03E178.SRTMGL1.hgt.zip', 'S03E179.SRTMGL1.hgt.zip',
                              'S03W180.SRTMGL1.hgt.zip', 'S03W179.SRTMGL1.hgt.zip',
                              'S02E177.SRTMGL1.hgt.zip', 'S02E178.SRTMGL1.hgt.zip', 'S02E179.SRTMGL1.hgt.zip',
                              'S02W180.SRTMGL1.hgt.zip', 'S02W179.SRTMGL1.hgt.zip',
                              'S01E177.SRTMGL1.hgt.zip', 'S01E178.SRTMGL1.hgt.zip', 'S01E179.SRTMGL1.hgt.zip',
                              'S01W180.SRTMGL1.hgt.zip', 'S01W179.SRTMGL1.hgt.zip',
                              'N00E177.SRTMGL1.hgt.zip', 'N00E178.SRTMGL1.hgt.zip', 'N00E179.SRTMGL1.hgt.zip',
                              'N00W180.SRTMGL1.hgt.zip', 'N00W179.SRTMGL1.hgt.zip',
                              'N01E177.SRTMGL1.hgt.zip', 'N01E178.SRTMGL1.hgt.zip', 'N01E179.SRTMGL1.hgt.zip',
                              'N01W180.SRTMGL1.hgt.zip', 'N01W179.SRTMGL1.hgt.zip']
        filenames = filename_generator.generate_filenames(btm_lat, top_lat, left_lon, right_lon)
        self.assertListEqual(filenames, expected_filenames)

    def test_gmt_all_quadrants(self):
        btm_lat = -1.5
        top_lat = 2.5
        left_lon = -1.5
        right_lon = 1.5
        expected_filenames = ['S02W002.SRTMGL1.hgt.zip', 'S02W001.SRTMGL1.hgt.zip', 'S02E000.SRTMGL1.hgt.zip',
                              'S02E001.SRTMGL1.hgt.zip',
                              'S01W002.SRTMGL1.hgt.zip', 'S01W001.SRTMGL1.hgt.zip', 'S01E000.SRTMGL1.hgt.zip',
                              'S01E001.SRTMGL1.hgt.zip',
                              'N00W002.SRTMGL1.hgt.zip', 'N00W001.SRTMGL1.hgt.zip', 'N00E000.SRTMGL1.hgt.zip',
                              'N00E001.SRTMGL1.hgt.zip',
                              'N01W002.SRTMGL1.hgt.zip', 'N01W001.SRTMGL1.hgt.zip', 'N01E000.SRTMGL1.hgt.zip',
                              'N01E001.SRTMGL1.hgt.zip',
                              'N02W002.SRTMGL1.hgt.zip', 'N02W001.SRTMGL1.hgt.zip', 'N02E000.SRTMGL1.hgt.zip',
                              'N02E001.SRTMGL1.hgt.zip']
        filenames = filename_generator.generate_filenames(btm_lat, top_lat, left_lon, right_lon)
        self.assertListEqual(filenames, expected_filenames)

    def test_that_wrap_between_west_180_and_east_180_gives_correct_values(self):
        result = filename_generator.wrap_longitude_between_west_180_and_east_179(50.5)
        self.assertEqual(result, 50.5)
        result = filename_generator.wrap_longitude_between_west_180_and_east_179(-50.5)
        self.assertEqual(result, -50.5)
        result = filename_generator.wrap_longitude_between_west_180_and_east_179(200)
        self.assertEqual(result, -160)
        result = filename_generator.wrap_longitude_between_west_180_and_east_179(300)
        self.assertEqual(result, -60)
        result = filename_generator.wrap_longitude_between_west_180_and_east_179(-200)
        self.assertEqual(result, 160)
        result = filename_generator.wrap_longitude_between_west_180_and_east_179(-300)
        self.assertEqual(result, 60)
        result = filename_generator.wrap_longitude_between_west_180_and_east_179(0)
        self.assertEqual(result, 0)
        result = filename_generator.wrap_longitude_between_west_180_and_east_179(180)
        self.assertEqual(result, -180)
        result = filename_generator.wrap_longitude_between_west_180_and_east_179(179)
        self.assertEqual(result, 179)
        result = filename_generator.wrap_longitude_between_west_180_and_east_179(-180)
        self.assertEqual(result, -180)

    def test_that_get_degrees_between_longitudes_gives_correct_values(self):
        result = filename_generator.get_degrees_between_longitudes(20, 30)
        self.assertEqual(result, 10)
        result = filename_generator.get_degrees_between_longitudes(-30, -20)
        self.assertEqual(result, 10)
        result = filename_generator.get_degrees_between_longitudes(-10, 10)
        self.assertEqual(result, 20)
        result = filename_generator.get_degrees_between_longitudes(177, -177)
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
