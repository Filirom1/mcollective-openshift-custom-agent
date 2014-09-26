module MCollective
  module Agent
    class OpenShift_custom<RPC::Agent

      def list_last_access_action
        reply[:msg] = Dir.glob('/var/lib/openshift/.last_access/*').map { |file|  { :uuid => File.basename(file), :last_access => File.read(file).chomp } }
      end
    end
  end
end
