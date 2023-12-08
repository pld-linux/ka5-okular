#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.4
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		okular
Summary:	KDE universal document viewer
Name:		ka5-%{kaname}
Version:	23.08.4
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	c0920c6d590f17b9520e471b1508f867
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	chmlib-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	djvulibre-devel
BuildRequires:	ebook-tools-devel
BuildRequires:	exiv2-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-tools
BuildRequires:	ka5-kdegraphics-mobipocket-devel >= %{version}
BuildRequires:	ka5-libkexiv2-devel >= %{version}
BuildRequires:	kf5-kactivities-devel >= %{kframever}
BuildRequires:	kf5-khtml-devel >= %{kframever}
BuildRequires:	kf5-kirigami2-devel >= %{kframever}
BuildRequires:	kf5-kpty-devel >= %{kframever}
BuildRequires:	kf5-purpose-devel >= %{kframever}
BuildRequires:	kf5-threadweaver-devel >= %{kframever}
BuildRequires:	kp5-libkscreen-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmarkdown-devel >= 2.2.6
BuildRequires:	libspectre-devel
BuildRequires:	libtiff-devel
BuildRequires:	libzip-devel
BuildRequires:	ninja
BuildRequires:	poppler-qt5-devel
BuildRequires:	qca-qt5-devel
BuildRequires:	qt5-build >= %{qtver}
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
%ghost %{_libdir}/libOkular5Core.so.1?
%attr(755,root,root) %{_libdir}/libOkular5Core.so.*.*.*
%dir %{_libdir}/qt5/plugins/okular
%dir %{_libdir}/qt5/plugins/okular/generators
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_chmlib.so
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_comicbook.so
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_djvu.so
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_dvi.so
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_epub.so
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_fax.so
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_fb.so
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_ghostview.so
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_kimgio.so
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_md.so
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_plucker.so
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_poppler.so
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_tiff.so
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_txt.so
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_xps.so
%{_libdir}/qt5/plugins/okularpart.so
%{_libdir}/qt5/plugins/okular/generators/okularGenerator_mobi.so
%{_libdir}/qt5/plugins/kf5/kio/kio_msits.so

%files data -f %{kaname}.lang
%defattr(644,root,root,755)
%{_desktopdir}/okularApplication_kimgio.desktop
%{_desktopdir}/org.kde.mobile.okular_kimgio.desktop
%{_desktopdir}/okularApplication_chm.desktop
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
%{_desktopdir}/org.kde.mobile.okular_chm.desktop
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
%{_iconsdir}/hicolor/128x128/apps/okular.png
%{_iconsdir}/hicolor/16x16/apps/okular.png
%{_iconsdir}/hicolor/22x22/apps/okular.png
%{_iconsdir}/hicolor/32x32/apps/okular.png
%{_iconsdir}/hicolor/48x48/apps/okular.png
%{_iconsdir}/hicolor/64x64/apps/okular.png
%{_datadir}/kconf_update/okular.upd
%{_datadir}/kservices5/okularChm.desktop
%{_datadir}/kservices5/okularComicbook.desktop
%{_datadir}/kservices5/okularDjvu.desktop
%{_datadir}/kservices5/okularDvi.desktop
%{_datadir}/kservices5/okularEPub.desktop
%{_datadir}/kservices5/okularFax.desktop
%{_datadir}/kservices5/okularFb.desktop
%{_datadir}/kservices5/okularGhostview.desktop
%{_datadir}/kservices5/okularMd.desktop
%{_datadir}/kservices5/okularPlucker.desktop
%{_datadir}/kservices5/okularPoppler.desktop
%{_datadir}/kservices5/okularTiff.desktop
%{_datadir}/kservices5/okularTxt.desktop
%{_datadir}/kservices5/okularXps.desktop
%{_datadir}/kservices5/okular_part.desktop
%{_datadir}/kservicetypes5/okularGenerator.desktop
%dir %{_datadir}/kxmlgui5/okular
%{_datadir}/kxmlgui5/okular/part-viewermode.rc
%{_datadir}/kxmlgui5/okular/part.rc
%{_datadir}/kxmlgui5/okular/shell.rc
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
%{_mandir}/uk/man1/okular.1*
%{_datadir}/metainfo/org.kde.okular-chm.metainfo.xml
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
%dir %{_datadir}/okular
%{_datadir}/okular/drawingtools.xml
%dir %{_datadir}/okular/icons
%dir %{_datadir}/okular/icons/hicolor
%dir %{_datadir}/okular/icons/hicolor/16x16
%dir %{_datadir}/okular/icons/hicolor/16x16/apps
%{_datadir}/okular/icons/hicolor/16x16/apps/okular-fb2.png
%{_datadir}/okular/icons/hicolor/16x16/apps/okular-gv.png
%dir %{_datadir}/okular/icons/hicolor/32x32
%dir %{_datadir}/okular/icons/hicolor/32x32/apps
%{_datadir}/okular/icons/hicolor/32x32/apps/okular-fb2.png
%{_datadir}/okular/icons/hicolor/32x32/apps/okular-gv.png
%dir %{_datadir}/okular/icons/hicolor/48x48
%dir %{_datadir}/okular/icons/hicolor/48x48/apps
%{_datadir}/okular/icons/hicolor/48x48/apps/okular-fb2.png
%dir %{_datadir}/okular/pics
%{_datadir}/okular/pics/checkmark.png
%{_datadir}/okular/pics/circle.png
%{_datadir}/okular/pics/comment.png
%{_datadir}/okular/pics/cross.png
%{_datadir}/okular/pics/help.png
%{_datadir}/okular/pics/insert.png
%{_datadir}/okular/pics/key.png
%{_datadir}/okular/pics/newparagraph.png
%{_datadir}/okular/pics/note.png
%{_datadir}/okular/pics/okular-epub-movie.png
%{_datadir}/okular/pics/okular-epub-sound-icon.png
%{_datadir}/okular/pics/paperclip.png
%{_datadir}/okular/pics/paragraph.png
%{_datadir}/okular/pics/pushpin.png
%{_datadir}/okular/pics/rightarrow.png
%{_datadir}/okular/pics/rightpointer.png
%{_datadir}/okular/pics/stamps.svg
%{_datadir}/okular/pics/star.png
%{_datadir}/okular/pics/tool-base-okular.png
%{_datadir}/okular/pics/tool-highlighter-okular-colorizable.png
%{_datadir}/okular/pics/tool-ink-okular-colorizable.png
%{_datadir}/okular/pics/tool-note-inline-okular-colorizable.png
%{_datadir}/okular/pics/tool-note-inline.png
%{_datadir}/okular/pics/tool-note-okular-colorizable.png
%{_datadir}/okular/pics/tool-note.png
%{_datadir}/okular/pics/uparrow.png
%{_datadir}/okular/pics/upleftarrow.png
%{_datadir}/okular/pics/tool-base-okular@2x.png
%{_datadir}/okular/pics/tool-highlighter-okular-colorizable@2x.png
%{_datadir}/okular/pics/tool-ink-okular-colorizable@2x.png
%{_datadir}/okular/pics/tool-note-inline-okular-colorizable@2x.png
%{_datadir}/okular/pics/tool-note-okular-colorizable@2x.png
%{_datadir}/okular/tools.xml
%{_datadir}/okular/toolsQuick.xml
%{_datadir}/kservices5/okularKimgio.desktop
%{_datadir}/metainfo/org.kde.okular-kimgio.metainfo.xml
%{_datadir}/okular/pics/tool-typewriter-okular-colorizable.png
%{_datadir}/okular/pics/tool-typewriter-okular-colorizable@2x.png
%{_desktopdir}/okularApplication_mobi.desktop
%{_desktopdir}/org.kde.mobile.okular_mobi.desktop
%{_datadir}/kservices5/okularMobi.desktop
%{_datadir}/metainfo/org.kde.okular-mobipocket.metainfo.xml
%{_datadir}/qlogging-categories5/okular.categories

%files devel
%defattr(644,root,root,755)
%{_libdir}/libOkular5Core.so
%{_libdir}/cmake/Okular5
%{_includedir}/okular
