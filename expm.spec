# Copyright 2013, Nathan Milford
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# To Install:
# sudo yum -y install rpmdevtools && rpmdev-setuptree
# wget https://raw.github.com/nmilford/rpm-expm/master/expm.spec -O ~/rpmbuild/SPECS/expm.spec
# wget http://expm.co/__download__/expm -O ~/rpmbuild/SOURCES/expm
# rpmbuild -bb ~/rpmbuild/SPECS/expm.spec

Name:      expm
Version:   0.1
Release:   1
Summary:   Elixir Package Manager
License:   Apache 2.0
URL:       https://github.com/yrashk/expm
Group:     Development/Tools
Source0:   http://expm.co/__download__/expm
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
Packager:  Nathan Milford <nathan@milford.io>
Requires: erlang
Requires: elixir

%description
Simplistic package manager for Erlang & Elixir programming languages

%prep

%build
rm -rf %{buildroot}
%install
install -d -m 755 %{buildroot}/%{_bindir}
install    -m 755 %_sourcedir/%{name} %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}

%changelog
* Fri Aug 16 2013 Nathan Milford <nathan@milford.io> 0.1-1
- Initial spec.