%if 0%{?fedora}%{?rhel} <= 6
    %global scl ruby193
    %global scl_prefix ruby193-
    %global vendor_ruby /opt/rh/%{scl}/root/usr/share/ruby/vendor_ruby/
    %global mco_agent_root /opt/rh/%{scl}/root/usr/libexec/mcollective/mcollective/agent/
%else
    %global vendor_ruby /usr/share/ruby/vendor_ruby/
    %global mco_agent_root /usr/libexec/mcollective/mcollective/agent/
%endif

Name:		mcollective-openshift-custom-agent
Version:	0.1
Release:	1%{?dist}
Summary:	A custom mcollective agent that interacts with OpenShift

Group:		
License:	ASL 2.0
URL:		https://github.com/Filirom1/mcollective-agent-openshift-custom
Source0:	https://github.com/Filirom1/mcollective-agent-openshift-custom/archive/master.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires:	ruby
Requires:	mcollective

%description
A custom mcollective agent that interacts with OpenShift

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{mco_agent_root}
cp -p mcollective/agent/openshift-custom.rb %{buildroot}%{mco_agent_root}
cp -p mcollective/agent/openshift-custom.ddl %{buildroot}%{mco_agent_root}

%files
%{mco_agent_root}openshift.rb
%{mco_agent_root}openshift.ddl

%changelog
