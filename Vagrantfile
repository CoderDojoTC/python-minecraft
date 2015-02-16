# -*- mode: ruby -*-
# vi: set ft=ruby :

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!! YOU MUST CONFIGURE SOME SETTINGS BEFORE YOU CAN USE THIS !!!!!
# !!!!! Read below under the CONFIGURE BEFORE USE heading.       !!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# This Vagrantfile sets up a python-minecraft lab server
# environment. This is the same environment used during our CoderDojo
# classroom events. For more details, visit the documentation at:
#
# http://python-minecraft.readthedocs.org/en/latest/other-setups/vagrant.html
#
# CONFIGURE BEFORE USE
#
# Some settings must be added to a file named "private_config.yaml" in
# the top level directory before you start up the environment using
# Vagrant. Open the file named "sample_config.yaml", save it to a new
# file named "private_config.yaml", and make the necessary edits. Read
# the documentation linked above for more support.

# This lab server environment uses Docker to create a
# private environment for each student. Each environment consists of a
# CanaryMod server, configured with the RaspberryJuice plugin, and set
# up to host a Minecraft world. It also includes an IPython Notebook
# server, configured to allow students to work through the exercises
# of the python-minecraft code group.

require 'yaml'

current_dir    = File.dirname(File.expand_path(__FILE__))
private_config = YAML.load_file("#{current_dir}/private_config.yaml")


# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  config.vm.provider "docker" do |d|
    d.image = private_config['image_name']
    d.ports = ["10443:8888", "10565:25565"]
    d.env = {
      "MOJANG_ACCOUNTS" => private_config['mojang_account'],
      "STUDENT_PASSWORD" => private_config['ipython_password'],
      "CODERDOJO_REPO" => private_config['coderdojo_source_code'],
    }
  end
end
