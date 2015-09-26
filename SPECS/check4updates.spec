Name:           check4updates
Version:        2015.09.26
Release:        1
Summary:        Weekly mails about available updates
License:        GPL
URL:            https://github.com/bcleonard/check4updates
Source0:        check4updates.cron
Source1:        check4updates
Source3:        check4updates.sysconfig
BuildArch: noarch
Requires: bash
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
check4updates from atrpms.net.  I found that after atrpms.net died, this was really the
only program that I used.  This is based on 77-1.

%prep
#%setup -q

%install
rm -rf $RPM_BUILD_ROOT
#%make_install
mkdir -p %{buildroot}%{_sysconfdir}/cron.weekly
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -p %{SOURCE0} %{buildroot}%{_sysconfdir}/cron.weekly/0check4updates
install -p -m 0755 %{SOURCE1} %{buildroot}%{_sbindir}/check4updates
install -p -m 0755 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/check4updates

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/sysconfig/check4updates
%{_sysconfdir}/cron.weekly/0check4updates
%{_sbindir}/check4updates

%doc

%clean
rm -rf %{buildroot}

%changelog
* Sat Sep 26 2015 Bradley Leonard <bradley@stygianresearch.com>
- Initial version
