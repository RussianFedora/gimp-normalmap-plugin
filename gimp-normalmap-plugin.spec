Name:           gimp-normalmap-plugin
Version:        1.2.2
Release:        1%{?dist}
Summary:        A plugin for GIMP for work with normal maps
Summary(ru):    Плагин GIMP для работы с картами нормалей

License:        GPLv2
URL:            http://code.google.com/p/gimp-normalmap/
Source0:        http://gimp-normalmap.googlecode.com/files/gimp-normalmap-%{version}.tar.bz2
Source100:      README.RFRemix

BuildRequires:  gimp-devel >= 2.4.0
BuildRequires:  glew-devel >= 1.3.3
BuildRequires:  gtkglext-devel >= 0.7.1
BuildRequires:  pkgconfig
BuildRequires:  gtk+-devel

Requires:       gimp >= 2.4

%description
A plugin for GIMP that aids in the authoring of tangent-space
normal maps for use in per-pixel lighting applications.

%description -l ru
Плагин для GIMP, помогающий работать с картами нормалей для использования
попиксельного освещения.


%prep
%setup -q -n gimp-normalmap-%{version}


%build
sed -i 's|-lGLEW|-lGLEW -lm|' Makefile.linux
make %{?_smp_mflags}
cp %{SOURCE100} .


%install
rm -rf $RPM_BUILD_ROOT
GIMP_PLUGINS_DIR=`gimptool-2.0 --gimpplugindir`
mkdir -p $RPM_BUILD_ROOT$GIMP_PLUGINS_DIR/plug-ins
install normalmap $RPM_BUILD_ROOT$GIMP_PLUGINS_DIR/plug-ins


%files
%defattr(-,root,root,-)
%{_libdir}/gimp/2.0/plug-ins/normalmap
%doc COPYING README README.RFRemix


%changelog
* Mon Jan 30 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 1.2.2-1.R
- initial release
