Name:           ros-indigo-yocs-virtual-sensor
Version:        0.6.3
Release:        0%{?dist}
Summary:        ROS yocs_virtual_sensor package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/yocs_virtual_sensor
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rospy-message-converter
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-tf
Requires:       ros-indigo-visualization-msgs
Requires:       ros-indigo-yocs-math-toolkit
Requires:       ros-indigo-yocs-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-yocs-math-toolkit
BuildRequires:  ros-indigo-yocs-msgs

%description
Virtual sensor that uses semantic map information to &quot;see&quot; obstacles
undetectable by robot sensors. Current implementation cannot read obstacles from
YAML files. Until this feature gets implemented, we use auxiliary scripts to
read and publish files' content. Data directory contains some example files.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Dec 05 2014 Jihoon Lee <jihoonl@yujinrobot.com> - 0.6.3-0
- Autogenerated by Bloom

* Sun Nov 30 2014 Jihoon Lee <jihoonl@yujinrobot.com> - 0.6.2-0
- Autogenerated by Bloom

