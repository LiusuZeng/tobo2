class CredentialType(object):
    NONE_TYPE = 0
    CERT_MUTUAL_AUTH = 1
    IAM_CREDS = 2


class AwsIotCredentialProvider(object):

    def __init__(self):
        object.__init__(self)
        self.credential_type = CredentialType.NONE_TYPE


class CertificateCredentialProvider(AwsIotCredentialProvider):

    def __init__(self, ca_path, cert_path, key_path):
        AwsIotCredentialProvider.__init__(self)
        self.credential_type = CredentialType.CERT_MUTUAL_AUTH
        self.__ca_path = ca_path
        self.__cert_path = cert_path
        self.__key_path = key_path

    def get_ca_path(self):
        return self.__ca_path

    def get_cert_path(self):
        return self.__cert_path

    def get_key_path(self):
        return self.__key_path


class IAMCredentialProvider(AwsIotCredentialProvider):

    def __init__(self, key_id="", secret_key="", session_token=""):
        AwsIotCredentialProvider.__init__(self)
        self._key_id = key_id
        self._secret_key = secret_key
        self._session_token = session_token

    def get_key_id(self):
        return self._key_id

    def get_secret_key(self):
        return self._secret_key

    def get_session_token(self):
        return self._session_token


class DefaultIAMCredentialProvider(IAMCredentialProvider):

    def __init__(self):
        IAMCredentialProvider.__init__(self)

    def _load_creds(self):
        pass

    def _is_creds_available(self):
        pass

    def _load_creds_from_env_var(self):
        pass

    def _load_creds_from_ini(self):
        pass
