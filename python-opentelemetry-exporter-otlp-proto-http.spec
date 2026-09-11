Name:           python-opentelemetry-exporter-otlp-proto-http
# Pinned to 1.39.1 to match the OpenTelemetry stack (base opentelemetry-api is
# 1.39.1). This exporter pins opentelemetry-{api,sdk,proto} and
# opentelemetry-exporter-otlp-proto-common to compatible 1.39.x versions, so it
# tracks them rather than the latest PyPI release. Its HTTP transport uses
# requests (the pin is ~=2.7).
Version:        1.39.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        OpenTelemetry Collector Protobuf over HTTP Exporter

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/main/exporter/opentelemetry-exporter-otlp-proto-http
Source:         %{pypi_source opentelemetry_exporter_otlp_proto_http}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'opentelemetry-exporter-otlp-proto-http' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-opentelemetry-exporter-otlp-proto-http
Summary:        %{summary}

%description -n python3-opentelemetry-exporter-otlp-proto-http %_description

# The gcp-auth extra (Google Cloud credential support) is not needed by vLLM and
# is not packaged, matching the rest of this OpenTelemetry stack, which ships no
# extras.


%prep
%autosetup -p1 -n opentelemetry_exporter_otlp_proto_http-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Automatically extracted from wheel
%pyproject_save_files -l opentelemetry


%check
%pyproject_check_import


%files -n python3-opentelemetry-exporter-otlp-proto-http -f %{pyproject_files}


%changelog
%autochangelog
