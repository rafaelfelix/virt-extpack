Vagrant::Config.run do |config|

  # Builder
  config.vm.define :builder do |builder_config|
    builder_config.vm.box = "centos62-builder"
  end 

  # Test
  config.vm.define :test do |test_config|
    test_config.vm.box = "centos62"
  end 

end
