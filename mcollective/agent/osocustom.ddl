metadata :name        => "osocustom",
         :description => "Custom Agent that interacts with Openhift",
         :author      => "Filirom1",
         :license     => "Apache 2",
         :version     => "0.1",
         :url         => "https://github.com/Filirom1/mcollective-agent-openshift-custom",
         :timeout     => 60

action "list_last_access", :description => "List last access time for each gears" do
   output :msg,
          :description => "Gear UUID and last access",
          :display_as  => "Message"
end
