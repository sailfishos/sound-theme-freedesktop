Name: sound-theme-freedesktop
Version: 0.8
Release: 2
Summary: Sound theme from freedesktop.org
Source0: http://people.freedesktop.org/~mccann/dist/sound-theme-freedesktop-%{version}.tar.bz2
Source1: index.theme
# For details on the licenses used, see README
License: GPLv2+ and LGPLv2+ and CC-BY-SA and CC-BY
Url: http://www.freedesktop.org/wiki/Specifications/sound-theme-spec
BuildArch: noarch
BuildRequires: gettext
BuildRequires: intltool >= 0.40
BuildRequires: pkgconfig(glib-2.0)
Requires(post): /bin/touch
Requires(postun): /bin/touch

%description
The default freedesktop.org sound theme following the XDG theming
specification.  (http://0pointer.de/public/sound-theme-spec.html).

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
%autogen

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
install -m 0644 %SOURCE1 %{buildroot}%{_datadir}/sounds/freedesktop/index.theme
 

%clean
rm -rf $RPM_BUILD_ROOT

%post
/bin/touch --no-create %{_datadir}/sounds/freedesktop %{_datadir}/sounds

%postun
/bin/touch --no-create %{_datadir}/sounds/freedesktop %{_datadir}/sounds

%files
%defattr(-,root,root)
%license CREDITS
%doc README
%dir %{_datadir}/sounds/freedesktop
%dir %{_datadir}/sounds/freedesktop/stereo
%{_datadir}/sounds/freedesktop/index.theme
%{_datadir}/sounds/freedesktop/stereo/*.oga

