Name:           ooumask
Version:        0.1.0
Release:        1%{?dist}
Summary:        Reads and sets the process file mode creation mask for spawned tasks.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooumask
Source0:        ooumask-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooumask is a sovereign, capability-bounded MASK CONTROLLER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooumask
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooumask-uninstall

%files
/usr/bin/ooumask
/usr/bin/ooumask-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
