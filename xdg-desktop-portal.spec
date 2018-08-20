#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xdg-desktop-portal
Version  : 1.0
Release  : 6
URL      : https://github.com/flatpak/xdg-desktop-portal/releases/download/1.0/xdg-desktop-portal-1.0.tar.xz
Source0  : https://github.com/flatpak/xdg-desktop-portal/releases/download/1.0/xdg-desktop-portal-1.0.tar.xz
Summary  : Desktop integration portal
Group    : Development/Tools
License  : LGPL-2.1
Requires: xdg-desktop-portal-config
Requires: xdg-desktop-portal-bin
Requires: xdg-desktop-portal-data
Requires: xdg-desktop-portal-license
Requires: xdg-desktop-portal-locales
Requires: xdg-desktop-portal-gtk
BuildRequires : gettext
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(flatpak)
BuildRequires : pkgconfig(fuse)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : sed
BuildRequires : xmlto

%description
# xdg-desktop-portal
A portal frontend service for [Flatpak](http://www.flatpak.org) and possibly
other desktop containment frameworks.

%package bin
Summary: bin components for the xdg-desktop-portal package.
Group: Binaries
Requires: xdg-desktop-portal-data
Requires: xdg-desktop-portal-config
Requires: xdg-desktop-portal-license

%description bin
bin components for the xdg-desktop-portal package.


%package config
Summary: config components for the xdg-desktop-portal package.
Group: Default

%description config
config components for the xdg-desktop-portal package.


%package data
Summary: data components for the xdg-desktop-portal package.
Group: Data

%description data
data components for the xdg-desktop-portal package.


%package dev
Summary: dev components for the xdg-desktop-portal package.
Group: Development
Requires: xdg-desktop-portal-bin
Requires: xdg-desktop-portal-data
Provides: xdg-desktop-portal-devel

%description dev
dev components for the xdg-desktop-portal package.


%package license
Summary: license components for the xdg-desktop-portal package.
Group: Default

%description license
license components for the xdg-desktop-portal package.


%package locales
Summary: locales components for the xdg-desktop-portal package.
Group: Default

%description locales
locales components for the xdg-desktop-portal package.


%prep
%setup -q -n xdg-desktop-portal-1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534776853
%configure --disable-static --disable-pipewire --disable-docbook-docs
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1534776853
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/xdg-desktop-portal
cp COPYING %{buildroot}/usr/share/doc/xdg-desktop-portal/COPYING
%make_install
%find_lang xdg-desktop-portal

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/libexec/xdg-desktop-portal
/usr/libexec/xdg-document-portal
/usr/libexec/xdg-permission-store

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/user/xdg-desktop-portal.service
/usr/lib/systemd/user/xdg-document-portal.service
/usr/lib/systemd/user/xdg-permission-store.service

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Access.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Account.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.AppChooser.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Email.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.FileChooser.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Inhibit.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Notification.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.PermissionStore.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Print.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.RemoteDesktop.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Request.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.ScreenCast.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Screenshot.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Session.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Account.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Device.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Documents.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Email.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.FileChooser.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Inhibit.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.NetworkMonitor.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Notification.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.OpenURI.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Print.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.ProxyResolver.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.RemoteDesktop.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Request.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.ScreenCast.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Screenshot.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Session.xml
/usr/share/dbus-1/services/org.freedesktop.impl.portal.PermissionStore.service
/usr/share/dbus-1/services/org.freedesktop.portal.Desktop.service
/usr/share/dbus-1/services/org.freedesktop.portal.Documents.service

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/xdg-desktop-portal.pc

%files license
%defattr(-,root,root,-)
/usr/share/doc/xdg-desktop-portal/COPYING

%files locales -f xdg-desktop-portal.lang
%defattr(-,root,root,-)

