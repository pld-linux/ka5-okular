%define		kdeappsver	15.08.0
%define		qtver		5.3.2
%define		kaname		okular
Summary:	KDE universal document viewer
Name:		ka5-%{kaname}
Version:	15.08.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	72ab8422045b06cbf2e4988d618d60ce
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	ebook-tools-devel
BuildRequires:	exiv2-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-tools
# # unreleased/only in git
#BuildRequires: kf5-kexiv2-devel
BuildRequires:	kp5-libkscreen-devel
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libspectre-devel
BuildRequires:	libtiff-devel
BuildRequires:	qca-devel
BuildRequires:	qimageblitz-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE universal document viewer.

%prep
%setup -q -n %{kaname}-%{version}

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/okular
%attr(755,root,root) %ghost %{_libdir}/libokularcore.so.6
%attr(755,root,root) %{_libdir}/libokularcore.*.*.*
%dir %{_libdir}/kde4/imports/org/kde/okular
%attr(755,root,root) %{_libdir}/kde4/imports/org/kde/okular/libokularplugin.so
%{_libdir}/kde4/imports/org/kde/okular/qmldir
%attr(755,root,root) %{_libdir}/kde4/kio_msits.so
%attr(755,root,root) %{_libdir}/kde4/okularGenerator_chmlib.so
%attr(755,root,root) %{_libdir}/kde4/okularGenerator_comicbook.so
%attr(755,root,root) %{_libdir}/kde4/okularGenerator_djvu.so
%attr(755,root,root) %{_libdir}/kde4/okularGenerator_dvi.so
%attr(755,root,root) %{_libdir}/kde4/okularGenerator_epub.so
%attr(755,root,root) %{_libdir}/kde4/okularGenerator_fax.so
%attr(755,root,root) %{_libdir}/kde4/okularGenerator_fb.so
%attr(755,root,root) %{_libdir}/kde4/okularGenerator_ghostview.so
%attr(755,root,root) %{_libdir}/kde4/okularGenerator_kimgio.so
%attr(755,root,root) %{_libdir}/kde4/okularGenerator_mobi.so
%attr(755,root,root) %{_libdir}/kde4/okularGenerator_ooo.so
%attr(755,root,root) %{_libdir}/kde4/okularGenerator_plucker.so
%attr(755,root,root) %{_libdir}/kde4/okularGenerator_poppler.so
%attr(755,root,root) %{_libdir}/kde4/okularGenerator_tiff.so
%attr(755,root,root) %{_libdir}/kde4/okularGenerator_txt.so
%attr(755,root,root) %{_libdir}/kde4/okularGenerator_xps.so
%attr(755,root,root) %{_libdir}/kde4/okularpart.so
%{_desktopdir}/kde4/active-documentviewer*.desktop
%{_desktopdir}/kde4/okular*.desktop
%{_datadir}/apps/kconf_update/okular.upd
%{_datadir}/apps/okular
%{_datadir}/config.kcfg/gssettings.kcfg
%{_datadir}/config.kcfg/okular.kcfg
%{_datadir}/config.kcfg/okular_core.kcfg
%{_datadir}/config.kcfg/pdfsettings.kcfg
%{_iconsdir}/hicolor/*/apps/okular.png
%{_iconsdir}/hicolor/scalable/apps/okular.svgz
%{_datadir}/kde4/services/libokularGenerator*.desktop
%{_datadir}/kde4/services/msits.protocol
%{_datadir}/kde4/services/okular*.desktop
%{_datadir}/kde4/servicetypes/okularGenerator.desktop
%{_mandir}/man1/okular.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libokularcore.so
%{_includedir}/okular
%{_libdir}/cmake/Okular
