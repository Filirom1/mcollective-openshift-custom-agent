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
Version:	0.3
Release:	1%{?dist}
Summary:	A custom mcollective agent that interacts with OpenShift

Group:          System Environment/Daemons
License:	ASL 2.0
URL:		https://github.com/Filirom1/mcollective-agent-openshift-custom
Source0:	https://github.com/Filirom1/mcollective-agent-openshift-custom/archive/master.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires:	%{?scl:%scl_prefix}mcollective

%description
A custom mcollective agent that interacts with OpenShift

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{mco_agent_root}
cp -p mcollective/agent/openshift_custom.rb %{buildroot}%{mco_agent_root}
cp -p mcollective/agent/openshift_custom.ddl %{buildroot}%{mco_agent_root}

%clean
rm -rf %{buildroot}

%files
%{mco_agent_root}openshift_custom.rb
%{mco_agent_root}openshift_custom.ddl

%changelog
* Fri Sep 26 2014 Filirom1 <Filirom1@gmail.com> 0.3-1
- fix spec file (Filirom1@gmail.com)
- fix spec file (Filirom1@gmail.com)
- fix spec file (Filirom1@gmail.com)

* Fri Sep 26 2014 Filirom1 <Filirom1@gmail.com> 0.2-1
- new package built with tito

