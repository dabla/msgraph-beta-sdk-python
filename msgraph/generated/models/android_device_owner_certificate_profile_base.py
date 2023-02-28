from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_device_owner_trusted_root_certificate = lazy_import('msgraph.generated.models.android_device_owner_trusted_root_certificate')
certificate_validity_period_scale = lazy_import('msgraph.generated.models.certificate_validity_period_scale')
device_configuration = lazy_import('msgraph.generated.models.device_configuration')
extended_key_usage = lazy_import('msgraph.generated.models.extended_key_usage')
subject_alternative_name_type = lazy_import('msgraph.generated.models.subject_alternative_name_type')
subject_name_format = lazy_import('msgraph.generated.models.subject_name_format')

class AndroidDeviceOwnerCertificateProfileBase(device_configuration.DeviceConfiguration):
    @property
    def certificate_validity_period_scale(self,) -> Optional[certificate_validity_period_scale.CertificateValidityPeriodScale]:
        """
        Gets the certificateValidityPeriodScale property value. Certificate Validity Period Options.
        Returns: Optional[certificate_validity_period_scale.CertificateValidityPeriodScale]
        """
        return self._certificate_validity_period_scale
    
    @certificate_validity_period_scale.setter
    def certificate_validity_period_scale(self,value: Optional[certificate_validity_period_scale.CertificateValidityPeriodScale] = None) -> None:
        """
        Sets the certificateValidityPeriodScale property value. Certificate Validity Period Options.
        Args:
            value: Value to set for the certificate_validity_period_scale property.
        """
        self._certificate_validity_period_scale = value
    
    @property
    def certificate_validity_period_value(self,) -> Optional[int]:
        """
        Gets the certificateValidityPeriodValue property value. Value for the Certificate Validity Period.
        Returns: Optional[int]
        """
        return self._certificate_validity_period_value
    
    @certificate_validity_period_value.setter
    def certificate_validity_period_value(self,value: Optional[int] = None) -> None:
        """
        Sets the certificateValidityPeriodValue property value. Value for the Certificate Validity Period.
        Args:
            value: Value to set for the certificate_validity_period_value property.
        """
        self._certificate_validity_period_value = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidDeviceOwnerCertificateProfileBase and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidDeviceOwnerCertificateProfileBase"
        # Certificate Validity Period Options.
        self._certificate_validity_period_scale: Optional[certificate_validity_period_scale.CertificateValidityPeriodScale] = None
        # Value for the Certificate Validity Period.
        self._certificate_validity_period_value: Optional[int] = None
        # Extended Key Usage (EKU) settings. This collection can contain a maximum of 500 elements.
        self._extended_key_usages: Optional[List[extended_key_usage.ExtendedKeyUsage]] = None
        # Certificate renewal threshold percentage. Valid values 1 to 99
        self._renewal_threshold_percentage: Optional[int] = None
        # Trusted Root Certificate.
        self._root_certificate: Optional[android_device_owner_trusted_root_certificate.AndroidDeviceOwnerTrustedRootCertificate] = None
        # Certificate Subject Alternative Name Type. Possible values are: none, emailAddress, userPrincipalName, customAzureADAttribute, domainNameService, universalResourceIdentifier.
        self._subject_alternative_name_type: Optional[subject_alternative_name_type.SubjectAlternativeNameType] = None
        # Certificate Subject Name Format. Possible values are: commonName, commonNameIncludingEmail, commonNameAsEmail, custom, commonNameAsIMEI, commonNameAsSerialNumber, commonNameAsAadDeviceId, commonNameAsIntuneDeviceId, commonNameAsDurableDeviceId.
        self._subject_name_format: Optional[subject_name_format.SubjectNameFormat] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceOwnerCertificateProfileBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerCertificateProfileBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidDeviceOwnerCertificateProfileBase()
    
    @property
    def extended_key_usages(self,) -> Optional[List[extended_key_usage.ExtendedKeyUsage]]:
        """
        Gets the extendedKeyUsages property value. Extended Key Usage (EKU) settings. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[extended_key_usage.ExtendedKeyUsage]]
        """
        return self._extended_key_usages
    
    @extended_key_usages.setter
    def extended_key_usages(self,value: Optional[List[extended_key_usage.ExtendedKeyUsage]] = None) -> None:
        """
        Sets the extendedKeyUsages property value. Extended Key Usage (EKU) settings. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the extended_key_usages property.
        """
        self._extended_key_usages = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "certificateValidityPeriodScale": lambda n : setattr(self, 'certificate_validity_period_scale', n.get_enum_value(certificate_validity_period_scale.CertificateValidityPeriodScale)),
            "certificateValidityPeriodValue": lambda n : setattr(self, 'certificate_validity_period_value', n.get_int_value()),
            "extendedKeyUsages": lambda n : setattr(self, 'extended_key_usages', n.get_collection_of_object_values(extended_key_usage.ExtendedKeyUsage)),
            "renewalThresholdPercentage": lambda n : setattr(self, 'renewal_threshold_percentage', n.get_int_value()),
            "rootCertificate": lambda n : setattr(self, 'root_certificate', n.get_object_value(android_device_owner_trusted_root_certificate.AndroidDeviceOwnerTrustedRootCertificate)),
            "subjectAlternativeNameType": lambda n : setattr(self, 'subject_alternative_name_type', n.get_enum_value(subject_alternative_name_type.SubjectAlternativeNameType)),
            "subjectNameFormat": lambda n : setattr(self, 'subject_name_format', n.get_enum_value(subject_name_format.SubjectNameFormat)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def renewal_threshold_percentage(self,) -> Optional[int]:
        """
        Gets the renewalThresholdPercentage property value. Certificate renewal threshold percentage. Valid values 1 to 99
        Returns: Optional[int]
        """
        return self._renewal_threshold_percentage
    
    @renewal_threshold_percentage.setter
    def renewal_threshold_percentage(self,value: Optional[int] = None) -> None:
        """
        Sets the renewalThresholdPercentage property value. Certificate renewal threshold percentage. Valid values 1 to 99
        Args:
            value: Value to set for the renewal_threshold_percentage property.
        """
        self._renewal_threshold_percentage = value
    
    @property
    def root_certificate(self,) -> Optional[android_device_owner_trusted_root_certificate.AndroidDeviceOwnerTrustedRootCertificate]:
        """
        Gets the rootCertificate property value. Trusted Root Certificate.
        Returns: Optional[android_device_owner_trusted_root_certificate.AndroidDeviceOwnerTrustedRootCertificate]
        """
        return self._root_certificate
    
    @root_certificate.setter
    def root_certificate(self,value: Optional[android_device_owner_trusted_root_certificate.AndroidDeviceOwnerTrustedRootCertificate] = None) -> None:
        """
        Sets the rootCertificate property value. Trusted Root Certificate.
        Args:
            value: Value to set for the root_certificate property.
        """
        self._root_certificate = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("certificateValidityPeriodScale", self.certificate_validity_period_scale)
        writer.write_int_value("certificateValidityPeriodValue", self.certificate_validity_period_value)
        writer.write_collection_of_object_values("extendedKeyUsages", self.extended_key_usages)
        writer.write_int_value("renewalThresholdPercentage", self.renewal_threshold_percentage)
        writer.write_object_value("rootCertificate", self.root_certificate)
        writer.write_enum_value("subjectAlternativeNameType", self.subject_alternative_name_type)
        writer.write_enum_value("subjectNameFormat", self.subject_name_format)
    
    @property
    def subject_alternative_name_type(self,) -> Optional[subject_alternative_name_type.SubjectAlternativeNameType]:
        """
        Gets the subjectAlternativeNameType property value. Certificate Subject Alternative Name Type. Possible values are: none, emailAddress, userPrincipalName, customAzureADAttribute, domainNameService, universalResourceIdentifier.
        Returns: Optional[subject_alternative_name_type.SubjectAlternativeNameType]
        """
        return self._subject_alternative_name_type
    
    @subject_alternative_name_type.setter
    def subject_alternative_name_type(self,value: Optional[subject_alternative_name_type.SubjectAlternativeNameType] = None) -> None:
        """
        Sets the subjectAlternativeNameType property value. Certificate Subject Alternative Name Type. Possible values are: none, emailAddress, userPrincipalName, customAzureADAttribute, domainNameService, universalResourceIdentifier.
        Args:
            value: Value to set for the subject_alternative_name_type property.
        """
        self._subject_alternative_name_type = value
    
    @property
    def subject_name_format(self,) -> Optional[subject_name_format.SubjectNameFormat]:
        """
        Gets the subjectNameFormat property value. Certificate Subject Name Format. Possible values are: commonName, commonNameIncludingEmail, commonNameAsEmail, custom, commonNameAsIMEI, commonNameAsSerialNumber, commonNameAsAadDeviceId, commonNameAsIntuneDeviceId, commonNameAsDurableDeviceId.
        Returns: Optional[subject_name_format.SubjectNameFormat]
        """
        return self._subject_name_format
    
    @subject_name_format.setter
    def subject_name_format(self,value: Optional[subject_name_format.SubjectNameFormat] = None) -> None:
        """
        Sets the subjectNameFormat property value. Certificate Subject Name Format. Possible values are: commonName, commonNameIncludingEmail, commonNameAsEmail, custom, commonNameAsIMEI, commonNameAsSerialNumber, commonNameAsAadDeviceId, commonNameAsIntuneDeviceId, commonNameAsDurableDeviceId.
        Args:
            value: Value to set for the subject_name_format property.
        """
        self._subject_name_format = value
    

