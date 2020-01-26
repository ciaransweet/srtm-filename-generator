import unittest

import filename_generator


class Tests(unittest.TestCase):

    def test_north_east(self):
        btm_lat = 1.5
        top_lat = 3.5
        left_lon = 1.5
        right_lon = 3.5
        expected_filenames = ['N01E001.hgt', 'N01E002.hgt', 'N01E003.hgt',
                              'N02E001.hgt', 'N02E002.hgt', 'N02E003.hgt',
                              'N03E001.hgt', 'N03E002.hgt', 'N03E003.hgt']
        filenames = filename_generator.main(btm_lat, top_lat, left_lon, right_lon)
        self.assertListEqual(filenames, expected_filenames)

    def test_north_west(self):
        btm_lat = 1.5
        top_lat = 3.5
        left_lon = -2.5
        right_lon = -0.5
        expected_filenames = ['N01W003.hgt', 'N01W002.hgt', 'N01W001.hgt',
                              'N02W003.hgt', 'N02W002.hgt', 'N02W001.hgt',
                              'N03W003.hgt', 'N03W002.hgt', 'N03W001.hgt']
        filenames = filename_generator.main(btm_lat, top_lat, left_lon, right_lon)
        self.assertListEqual(filenames, expected_filenames)

    def test_south_west(self):
        btm_lat = -10.5
        top_lat = -7.5
        left_lon = -120.5
        right_lon = -117.5
        expected_filenames = ['S11W121.hgt', 'S11W120.hgt', 'S11W119.hgt', 'S11W118.hgt',
                              'S10W121.hgt', 'S10W120.hgt', 'S10W119.hgt', 'S10W118.hgt',
                              'S09W121.hgt', 'S09W120.hgt', 'S09W119.hgt', 'S09W118.hgt',
                              'S08W121.hgt', 'S08W120.hgt', 'S08W119.hgt', 'S08W118.hgt']
        filenames = filename_generator.main(btm_lat, top_lat, left_lon, right_lon)
        self.assertListEqual(filenames, expected_filenames)

    def test_south_east(self):
        btm_lat = -10.5
        top_lat = -7.5
        left_lon = 117.5
        right_long = 120.5
        expected_filenames = ['S11E117.hgt', 'S11E118.hgt', 'S11E119.hgt', 'S11E120.hgt',
                              'S10E117.hgt', 'S10E118.hgt', 'S10E119.hgt', 'S10E120.hgt',
                              'S09E117.hgt', 'S09E118.hgt', 'S09E119.hgt', 'S09E120.hgt',
                              'S08E117.hgt', 'S08E118.hgt', 'S08E119.hgt', 'S08E120.hgt']
        filenames = filename_generator.main(btm_lat, top_lat, left_lon, right_long)
        self.assertListEqual(filenames, expected_filenames)

    def test_equator_cross_east(self):
        btm_lat = -1.5
        top_lat = 1.5
        left_lon = 1.5
        right_lon = 3.5
        expected_filenames = ['S02E001.hgt', 'S02E002.hgt', 'S02E003.hgt',
                              'S01E001.hgt', 'S01E002.hgt', 'S01E003.hgt',
                              'N00E001.hgt', 'N00E002.hgt', 'N00E003.hgt',
                              'N01E001.hgt', 'N01E002.hgt', 'N01E003.hgt']
        filenames = filename_generator.main(btm_lat, top_lat, left_lon, right_lon)
        self.assertListEqual(filenames, expected_filenames)

    def test_equator_cross_west(self):
        btm_lat = -1.5
        top_lat = 1.5
        left_lon = -3.5
        right_lon = -1.5
        expected_filenames = ['S02W004.hgt', 'S02W003.hgt', 'S02W002.hgt',
                              'S01W004.hgt', 'S01W003.hgt', 'S01W002.hgt',
                              'N00W004.hgt', 'N00W003.hgt', 'N00W002.hgt',
                              'N01W004.hgt', 'N01W003.hgt', 'N01W002.hgt']
        filenames = filename_generator.main(btm_lat, top_lat, left_lon, right_lon)
        self.assertListEqual(filenames, expected_filenames)

    def test_international_dateline_all_quadrants(self):
        btm_lat = -2.5
        top_lat = 1.5
        left_lon = 177.5
        right_lon = -178.5
        expected_filenames = ['S03E177.hgt', 'S03E178.hgt', 'S03E179.hgt', 'S03W180.hgt', 'S03W179.hgt',
                              'S02E177.hgt', 'S02E178.hgt', 'S02E179.hgt', 'S02W180.hgt', 'S02W179.hgt',
                              'S01E177.hgt', 'S01E178.hgt', 'S01E179.hgt', 'S01W180.hgt', 'S01W179.hgt',
                              'N00E177.hgt', 'N00E178.hgt', 'N00E179.hgt', 'N00W180.hgt', 'N00W179.hgt',
                              'N01E177.hgt', 'N01E178.hgt', 'N01E179.hgt', 'N01W180.hgt', 'N01W179.hgt']
        filenames = filename_generator.main(btm_lat, top_lat, left_lon, right_lon)
        self.assertListEqual(filenames, expected_filenames)

    def test_gmt_all_quadrants(self):
        btm_lat = -1.5
        top_lat = 2.5
        left_lon = -1.5
        right_lon = 1.5
        expected_filenames = ['S02W002.hgt', 'S02W001.hgt', 'S02E000.hgt', 'S02E001.hgt',
                              'S01W002.hgt', 'S01W001.hgt', 'S01E000.hgt', 'S01E001.hgt',
                              'N00W002.hgt', 'N00W001.hgt', 'N00E000.hgt', 'N00E001.hgt',
                              'N01W002.hgt', 'N01W001.hgt', 'N01E000.hgt', 'N01E001.hgt',
                              'N02W002.hgt', 'N02W001.hgt', 'N02E000.hgt', 'N02E001.hgt']
        filenames = filename_generator.main(btm_lat, top_lat, left_lon, right_lon)
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
