FILENAME_FORMAT = '{0}{1}{2}{3}.SRTMGL1.hgt.zip'


def generate_filenames(btm_lat, top_lat, left_lon, right_lon):
    filenames = []
    btm_lat_int = int(btm_lat)
    top_lat_int = int(top_lat)
    left_lon_int = int(left_lon)
    right_lon_int = int(right_lon)

    if btm_lat_int <= 0:
        btm_lat_int = btm_lat_int - 1
    if top_lat_int <= 0:
        top_lat_int = top_lat_int - 1
    if left_lon_int < 0:
        left_lon_int = left_lon_int - 1
    if right_lon_int <= 0:
        right_lon_int = right_lon_int - 1

    for lat in range(btm_lat_int, top_lat_int + 1):
        lat_hem = 'N' if lat >= 0 else 'S'
        lat_padded = str(abs(lat)).zfill(2)
        degrees_between = get_degrees_between_longitudes(left_lon_int, right_lon_int)
        for i in range(0, degrees_between + 1):
            wrapped_lon = wrap_longitude_between_west_180_and_east_179(left_lon_int + i)
            lon_hem = 'E' if wrapped_lon >= 0 else 'W'
            lon_padded = str(abs(wrapped_lon)).zfill(3)
            filename = FILENAME_FORMAT.format(lat_hem, lat_padded, lon_hem, lon_padded)
            filenames.append(filename)
    return filenames


def wrap_longitude_between_west_180_and_east_179(longitude):
    west_longitude_inclusive_limit = -180
    return ((longitude - west_longitude_inclusive_limit) % 360) % 360 + west_longitude_inclusive_limit


def get_degrees_between_longitudes(left_lon, right_lon):
    if left_lon >= 0 > right_lon:
        return (right_lon - left_lon) % 180
    else:
        return right_lon - left_lon
