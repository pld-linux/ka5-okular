#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.01.95
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		okular
Summary:	KDE universal document viewer
Name:		ka5-%{kaname}
Version:	24.01.95
Release:	0.1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/unstable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	afebfbe0ebfa6baee5da5b5f0b4b9df2
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	chmlib-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	djvulibre-devel
BuildRequires:	ebook-tools-devel
BuildRequires:	exiv2-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-tools
BuildRequires:	ka5-kdegraphics-mobipocket-devel >= %{version}
BuildRequires:	ka5-libkexiv2-devel >= %{version}
BuildRequires:	kf6-kirigami-devel >= %{kframever}
BuildRequires:	kf6-kpty-devel >= %{kframever}
BuildRequires:	kf6-purpose-devel >= %{kframever}
BuildRequires:	kf6-threadweaver-devel >= %{kframever}
BuildRequires:	kp5-libkscreen-devel
BuildRequires:	kp5-plasma-activities-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmarkdown-devel >= 2.2.6
BuildRequires:	libspectre-devel
BuildRequires:	libtiff-devel
BuildRequires:	libzip-devel
BuildRequires:	ninja
BuildRequires:	poppler-qt6-devel
BuildRequires:	qca-qt6-devel
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	%{name}-data = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Okular is a universal document viewer.

Features

• Several Supported Formats: PDF, PS, Tiff, CHM, DjVu, Images, DVI,
XPS, ODT, Fiction Book, Comic Book, Plucker, EPub, Fax • Thumbnails
sidebar • Annotations support

%description -l pl.UTF-8
Okular to uniwersalna przeglądarka dokumentów.

Właściwości

• Wiele wspieranych formatów: PDF, PS, Tiff, CHM, DjVu, Images, DVI,
XPS, ODT, Fiction Book, Comic Book, Plucker, EPub, Fax • Panel boczny
z miniaturkami • Wsparcie dla adnotacji

%package data
Summary:	Data files for %{kaname}
Summary(pl.UTF-8):	Dane dla %{kaname}
Group:		X11/Applications
BuildArch:	noarch

%description data
Data files for %{kaname}.

%description data -l pl.UTF-8
Dane dla %{kaname}.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir}
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

# not supported by glibc yet
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/okular
%ghost %{_libdir}/libOkular6Core.so.1
%attr(755,root,root) %{_libdir}/libOkular6Core.so.*.*
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/parts/okularpart.so
%dir %{_libdir}/qt6/plugins/okular_generators
%attr(755,root,root) %{_libdir}/qt6/plugins/okular_generators/okularGenerator_comicbook.so
%attr(755,root,root) %{_libdir}/qt6/plugins/okular_generators/okularGenerator_djvu.so
%attr(755,root,root) %{_libdir}/qt6/plugins/okular_generators/okularGenerator_dvi.so
%attr(755,root,root) %{_libdir}/qt6/plugins/okular_generators/okularGenerator_epub.so
%attr(755,root,root) %{_libdir}/qt6/plugins/okular_generators/okularGenerator_fax.so
%attr(755,root,root) %{_libdir}/qt6/plugins/okular_generators/okularGenerator_fb.so
%attr(755,root,root) %{_libdir}/qt6/plugins/okular_generators/okularGenerator_ghostview.so
%attr(755,root,root) %{_libdir}/qt6/plugins/okular_generators/okularGenerator_kimgio.so
%attr(755,root,root) %{_libdir}/qt6/plugins/okular_generators/okularGenerator_md.so
%attr(755,root,root) %{_libdir}/qt6/plugins/okular_generators/okularGenerator_mobi.so
%attr(755,root,root) %{_libdir}/qt6/plugins/okular_generators/okularGenerator_plucker.so
%attr(755,root,root) %{_libdir}/qt6/plugins/okular_generators/okularGenerator_poppler.so
%attr(755,root,root) %{_libdir}/qt6/plugins/okular_generators/okularGenerator_tiff.so
%attr(755,root,root) %{_libdir}/qt6/plugins/okular_generators/okularGenerator_txt.so
%attr(755,root,root) %{_libdir}/qt6/plugins/okular_generators/okularGenerator_xps.so

%files data -f %{kaname}.lang
%defattr(644,root,root,755)
%{_desktopdir}/okularApplication_kimgio.desktop
%{_desktopdir}/org.kde.mobile.okular_kimgio.desktop
%{_desktopdir}/okularApplication_comicbook.desktop
%{_desktopdir}/okularApplication_djvu.desktop
%{_desktopdir}/okularApplication_dvi.desktop
%{_desktopdir}/okularApplication_epub.desktop
%{_desktopdir}/okularApplication_fax.desktop
%{_desktopdir}/okularApplication_fb.desktop
%{_desktopdir}/okularApplication_ghostview.desktop
%{_desktopdir}/okularApplication_md.desktop
%{_desktopdir}/okularApplication_pdf.desktop
%{_desktopdir}/okularApplication_plucker.desktop
%{_desktopdir}/okularApplication_tiff.desktop
%{_desktopdir}/okularApplication_txt.desktop
%{_desktopdir}/okularApplication_xps.desktop
%{_desktopdir}/org.kde.mobile.okular_comicbook.desktop
%{_desktopdir}/org.kde.mobile.okular_djvu.desktop
%{_desktopdir}/org.kde.mobile.okular_dvi.desktop
%{_desktopdir}/org.kde.mobile.okular_epub.desktop
%{_desktopdir}/org.kde.mobile.okular_fax.desktop
%{_desktopdir}/org.kde.mobile.okular_fb.desktop
%{_desktopdir}/org.kde.mobile.okular_ghostview.desktop
%{_desktopdir}/org.kde.mobile.okular_md.desktop
%{_desktopdir}/org.kde.mobile.okular_pdf.desktop
%{_desktopdir}/org.kde.mobile.okular_plucker.desktop
%{_desktopdir}/org.kde.mobile.okular_tiff.desktop
%{_desktopdir}/org.kde.mobile.okular_txt.desktop
%{_desktopdir}/org.kde.mobile.okular_xps.desktop
%{_desktopdir}/org.kde.okular.desktop
%{_datadir}/config.kcfg/gssettings.kcfg
%{_datadir}/config.kcfg/okular.kcfg
%{_datadir}/config.kcfg/okular_core.kcfg
%{_datadir}/config.kcfg/pdfsettings.kcfg
%{_iconsdir}/hicolor/*x*/apps/okular.png
%{_datadir}/kconf_update/okular.upd
%{_mandir}/ca/man1/okular.1*
%{_mandir}/de/man1/okular.1*
%{_mandir}/es/man1/okular.1*
%{_mandir}/et/man1/okular.1*
%{_mandir}/fr/man1/okular.1*
%{_mandir}/it/man1/okular.1*
%{_mandir}/man1/okular.1*
%{_mandir}/nl/man1/okular.1*
%{_mandir}/pt/man1/okular.1*
%{_mandir}/pt_BR/man1/okular.1*
%{_mandir}/ru/man1/okular.1*
%{_mandir}/sv/man1/okular.1*
%{_mandir}/tr/man1/okular.1*
%{_mandir}/uk/man1/okular.1*
%{_datadir}/metainfo/org.kde.okular-comicbook.metainfo.xml
%{_datadir}/metainfo/org.kde.okular-djvu.metainfo.xml
%{_datadir}/metainfo/org.kde.okular-dvi.metainfo.xml
%{_datadir}/metainfo/org.kde.okular-epub.metainfo.xml
%{_datadir}/metainfo/org.kde.okular-fax.metainfo.xml
%{_datadir}/metainfo/org.kde.okular-fb.metainfo.xml
%{_datadir}/metainfo/org.kde.okular-md.metainfo.xml
%{_datadir}/metainfo/org.kde.okular-plucker.metainfo.xml
%{_datadir}/metainfo/org.kde.okular-poppler.metainfo.xml
%{_datadir}/metainfo/org.kde.okular-spectre.metainfo.xml
%{_datadir}/metainfo/org.kde.okular-tiff.metainfo.xml
%{_datadir}/metainfo/org.kde.okular-txt.metainfo.xml
%{_datadir}/metainfo/org.kde.okular-xps.metainfo.xml
%{_datadir}/metainfo/org.kde.okular.appdata.xml
%{_datadir}/okular
%{_datadir}/metainfo/org.kde.okular-kimgio.metainfo.xml
%{_desktopdir}/okularApplication_mobi.desktop
%{_desktopdir}/org.kde.mobile.okular_mobi.desktop
%{_datadir}/metainfo/org.kde.okular-mobipocket.metainfo.xml
%{_datadir}/qlogging-categories6/okular.categories

%files devel
%defattr(644,root,root,755)
%{_includedir}/okular
%{_libdir}/cmake/Okular6
%{_libdir}/libOkular6Core.so
