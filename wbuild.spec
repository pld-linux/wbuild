Summary:	Widget Building Tool
Summary(pl.UTF-8):   Narzędzie do budowania widgetów
Name:		wbuild
Version:	3.0
Release:	0.2
License:	(?)
Group:		Applications/X11
Source0:	http://www.ibiblio.org/pub/linux/X11/libs/fwf/%{name}-%{version}.tar.gz
# Source0-md5:	0303041e14e565091ff691b3e4481373
Patch0:		%{name}-DESTDIR.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Widget Building Tool.

%description -l pl.UTF-8
Narzędzie do budowania widgetów.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CFLAGS="%{rpmcflags} -DINITFILE='\"%{_sysconfdir}/wbuild.cfg\"' "\
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/wbuild
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/wbuild.cfg
