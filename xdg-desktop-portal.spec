#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : xdg-desktop-portal
Version  : 1.16.0
Release  : 30
URL      : https://github.com/flatpak/xdg-desktop-portal/releases/download/1.16.0/xdg-desktop-portal-1.16.0.tar.xz
Source0  : https://github.com/flatpak/xdg-desktop-portal/releases/download/1.16.0/xdg-desktop-portal-1.16.0.tar.xz
Summary  : Desktop integration portal
Group    : Development/Tools
License  : LGPL-2.1
Requires: xdg-desktop-portal-data = %{version}-%{release}
Requires: xdg-desktop-portal-libexec = %{version}-%{release}
Requires: xdg-desktop-portal-license = %{version}-%{release}
Requires: xdg-desktop-portal-locales = %{version}-%{release}
Requires: xdg-desktop-portal-services = %{version}-%{release}
Requires: pipewire
BuildRequires : bubblewrap
BuildRequires : buildreq-meson
BuildRequires : dbus-bin
BuildRequires : fuse-dev
BuildRequires : geoclue-dev
BuildRequires : gsettings-desktop-schemas
BuildRequires : json-glib-dev
BuildRequires : libportal-dev
BuildRequires : pipewire-dev
BuildRequires : pkgconfig(flatpak)
BuildRequires : pkgconfig(fuse3)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libgeoclue-2.0)
BuildRequires : pkgconfig(libportal)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(systemd)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
DO NOT MODIFY ANY FILE IN THIS DIRECTORY
(except maybe the Makefile.am)
This directory is the result of a git subtree merge with the 'gvdb'
module on git.gnome.org.  Please apply fixes to the 'gvdb' module and
perform a git merge.

%package data
Summary: data components for the xdg-desktop-portal package.
Group: Data

%description data
data components for the xdg-desktop-portal package.


%package dev
Summary: dev components for the xdg-desktop-portal package.
Group: Development
Requires: xdg-desktop-portal-data = %{version}-%{release}
Provides: xdg-desktop-portal-devel = %{version}-%{release}
Requires: xdg-desktop-portal = %{version}-%{release}

%description dev
dev components for the xdg-desktop-portal package.


%package libexec
Summary: libexec components for the xdg-desktop-portal package.
Group: Default
Requires: xdg-desktop-portal-license = %{version}-%{release}

%description libexec
libexec components for the xdg-desktop-portal package.


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


%package services
Summary: services components for the xdg-desktop-portal package.
Group: Systemd services
Requires: systemd

%description services
services components for the xdg-desktop-portal package.


%prep
%setup -q -n xdg-desktop-portal-1.16.0
cd %{_builddir}/xdg-desktop-portal-1.16.0
pushd ..
cp -a xdg-desktop-portal-1.16.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685480470
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
# Tests require some glib schemas to be initialized
target=$HOME/.local/share/glib-2.0/schemas
mkdir -p $target
glib-compile-schemas --targetdir=$target /usr/share/glib-2.0/schemas
export XDG_DATA_DIRS="$HOME/.local/share${XDG_DATA_DIRS:+:$XDG_DATA_DIRS}"
make %{?_smp_mflags} VERBOSE=1 V=1 check || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/xdg-desktop-portal
cp %{_builddir}/xdg-desktop-portal-%{version}/COPYING %{buildroot}/usr/share/package-licenses/xdg-desktop-portal/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang xdg-desktop-portal
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Access.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Account.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.AppChooser.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Background.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.DynamicLauncher.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Email.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.FileChooser.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.GlobalShortcuts.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Inhibit.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Lockdown.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Notification.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.PermissionStore.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Print.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.RemoteDesktop.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Request.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.ScreenCast.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Screenshot.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Secret.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Session.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Settings.xml
/usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Wallpaper.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Account.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Background.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Camera.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Device.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Documents.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.DynamicLauncher.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Email.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.FileChooser.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.FileTransfer.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.GameMode.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.GlobalShortcuts.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Inhibit.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Location.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.MemoryMonitor.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.NetworkMonitor.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Notification.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.OpenURI.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.PowerProfileMonitor.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Print.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.ProxyResolver.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Realtime.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.RemoteDesktop.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Request.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.ScreenCast.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Screenshot.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Secret.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Session.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Settings.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Trash.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Wallpaper.xml
/usr/share/dbus-1/services/org.freedesktop.impl.portal.PermissionStore.service
/usr/share/dbus-1/services/org.freedesktop.portal.Desktop.service
/usr/share/dbus-1/services/org.freedesktop.portal.Documents.service

%files dev
%defattr(-,root,root,-)
/usr/share/pkgconfig/xdg-desktop-portal.pc

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/xdg-desktop-portal
/V3/usr/libexec/xdg-desktop-portal-rewrite-launchers
/V3/usr/libexec/xdg-desktop-portal-validate-icon
/V3/usr/libexec/xdg-document-portal
/V3/usr/libexec/xdg-permission-store
/usr/libexec/xdg-desktop-portal
/usr/libexec/xdg-desktop-portal-rewrite-launchers
/usr/libexec/xdg-desktop-portal-validate-icon
/usr/libexec/xdg-document-portal
/usr/libexec/xdg-permission-store

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xdg-desktop-portal/01a6b4bf79aca9b556822601186afab86e8c4fbf

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/xdg-desktop-portal-rewrite-launchers.service
/usr/lib/systemd/user/xdg-desktop-portal.service
/usr/lib/systemd/user/xdg-document-portal.service
/usr/lib/systemd/user/xdg-permission-store.service

%files locales -f xdg-desktop-portal.lang
%defattr(-,root,root,-)

