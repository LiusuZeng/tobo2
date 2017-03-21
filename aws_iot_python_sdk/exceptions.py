class AwsIotException(Exception):

    def __init__(self, error_message):
        Exception.__init__(self)
        self.__error_message = error_message

    def get_error_message(self):
        return self.__error_message


class ErrorMessagePrefix(object):
    MQTT_EXCEPTION_ERROR_MESSAGE_PREFIX = "[MqttException] "
    SHADOW_EXCEPTION_ERROR_MESSAGE_PREFIX = "[ShadowException] "
    GREENGRASS_EXCEPTION_ERROR_MESSAGE_PREFIX = "[GreenGrassException] "


class MqttException(AwsIotException):

    def __init__(self, error_message):
        AwsIotException.__init__(self, ErrorMessagePrefix.MQTT_EXCEPTION_ERROR_MESSAGE_PREFIX + error_message)


class ShadowException(AwsIotException):

    def __init__(self, error_message):
        AwsIotException.__init__(self, ErrorMessagePrefix.SHADOW_EXCEPTION_ERROR_MESSAGE_PREFIX + error_message)


class GreenGrassException(AwsIotException):

    def __init__(self, error_message):
        AwsIotException.__init__(self, ErrorMessagePrefix.GREENGRASS_EXCEPTION_ERROR_MESSAGE_PREFIX + error_message)
