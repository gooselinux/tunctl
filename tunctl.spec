Name:           tunctl
Version:        1.5
Release:        3%{?dist}
Summary:        Create and remove virtual network interfaces

Group:          Applications/System
License:        GPL+
URL:            http://tunctl.sourceforge.net/
Source0:        http://downloads.sourceforge.net/tunctl/tunctl-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  docbook-utils

%description
tunctl is a tool to set up and maintain persistent TUN/TAP network
interfaces, enabling user applications access to the wire side of a
virtual nework interface. Such interfaces is useful for connecting VPN
software, virtualization, emulation and a number of other similar
applications to the network stack.

tunctl originates from the User Mode Linux project.

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
chmod -x $RPM_BUILD_ROOT%{_mandir}/man8/tunctl.8*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_mandir}/man8/tunctl.8*
%{_sbindir}/tunctl
%doc ChangeLog

%changelog
* Thu Oct 13 2008 Jiri Pirko <jpirko@redhat.com> 1.5-3
- Import from EPEL

* Thu Jul 18 2008 Henrik Nordstrom <henrik@henriknordstrom.net> 1.5-2
- Corrected package description formatting

* Wed Jul 16 2008 Henrik Nordstrom <henrik@henriknordstrom.net> 1.5-1
- Update to version 1.5 based on separate upstream release

* Tue Mar 25 2008 Lubomir Kundrak <lkundrak@redhat.com> 1.4-2
- Move to sbin (Marek Mahut, #434583)

* Fri Feb 22 2008 Lubomir Kundrak <lkundrak@redhat.com> 1.4-1
- Initial packaging
