%define prefix /usr/local

Summary: Bata Radio SK
Name: bata-radio-sk
Version: 0.1.0
Release: 1
BuildArch: noarch
License: Bata a.s
Vendor: Bata a.s
Packager: Pavel Barina <pavel.barina@bata.com>
Url: http://www.bata.com
Group: BATA
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-root
Requires: mplayer
Conflicts: bata-radio

%description
Bata Radio

%prep
%setup -q

%build

%install
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
install -m 0755 ./etc/rc.d/init.d/bata-radio $RPM_BUILD_ROOT/etc/rc.d/init.d

mkdir -p $RPM_BUILD_ROOT/usr/local/bin
install -m 0755 ./usr/local/bin/bata-radio-check $RPM_BUILD_ROOT%{prefix}/bin

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post
/etc/rc.d/init.d/bata-radio restart

%preun

%postun

%files
%defattr(-,root,root)
%attr(755,root,root) /etc/rc.d/init.d/bata-radio
%attr(755,root,root) /usr/local/bin/bata-radio-check

%changelog
* Fri Mar 09 2018 Bata a.s Pavel Barina <pavel.barina@bata.com> - 0.1.0-1
- uprava pro nonstop prehravani. Prejmenovani na Bata radio CZ nebo SK.
- slovensky balicek bata-radio-sk
