%define		kdeappsver	15.08.0
%define		qtver		5.3.2
%define		kaname		okular
Summary:	KDE universal document viewer
Name:		ka5-%{kaname}
Version:	15.08.0
Release:	0.1
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
BuildRequires:	ka5-libkexiv2-devel
BuildRequires:	kde4-libkexiv2-devel
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

#%find_lang %{kaname} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# -f %{kaname}.lang
#%attr(755,root,root) %{_bindir}/gwenview
#%attr(755,root,root) %{_libdir}/libgwenviewlib.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libgwenviewlib.so.5
#%attr(755,root,root)        %{_libdir}/qt5/plugins/gvpart.so
