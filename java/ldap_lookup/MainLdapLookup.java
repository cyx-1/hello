import com.unboundid.ldap.sdk.*;
import com.unboundid.ldap.sdk.controls.SubtreeDeleteRequestControl;
import com.unboundid.ldap.listener.*;
import java.util.*;

/**
 * LDAP Lookup Example using UnboundID LDAP SDK
 *
 * This example demonstrates:
 * 1. Connecting to an in-memory LDAP server
 * 2. Adding sample entries
 * 3. Searching for entries
 * 4. Retrieving and displaying attributes
 * 5. Performing filtered searches
 */
public class MainLdapLookup {

    public static void main(String[] args) {
        try {
            // Line 18-21: Create and start an in-memory LDAP server for demonstration
            System.out.println("=== LDAP Lookup Example ===\n");
            System.out.println("[1] Creating in-memory LDAP server...");
            InMemoryDirectoryServerConfig config = new InMemoryDirectoryServerConfig("dc=example,dc=com");
            config.addAdditionalBindCredentials("cn=admin,dc=example,dc=com", "password");
            InMemoryDirectoryServer ldapServer = new InMemoryDirectoryServer(config);
            ldapServer.startListening();
            System.out.println("    LDAP server started on port: " + ldapServer.getListenPort());

            // Line 26-28: Connect to the LDAP server
            System.out.println("\n[2] Connecting to LDAP server...");
            LDAPConnection connection = new LDAPConnection("localhost", ldapServer.getListenPort());
            System.out.println("    Connected successfully!");

            // Line 31-49: Add sample organizational structure
            System.out.println("\n[3] Adding sample LDAP entries...");

            // Add base entry
            connection.add(new AddRequest(
                "dn: dc=example,dc=com",
                "objectClass: top",
                "objectClass: domain",
                "dc: example"));

            // Add organizational unit for people
            connection.add(new AddRequest(
                "dn: ou=people,dc=example,dc=com",
                "objectClass: top",
                "objectClass: organizationalUnit",
                "ou: people"));

            // Add organizational unit for groups
            connection.add(new AddRequest(
                "dn: ou=groups,dc=example,dc=com",
                "objectClass: top",
                "objectClass: organizationalUnit",
                "ou: groups"));

            // Line 52-93: Add sample user entries
            connection.add(new AddRequest(
                "dn: uid=jdoe,ou=people,dc=example,dc=com",
                "objectClass: top",
                "objectClass: person",
                "objectClass: organizationalPerson",
                "objectClass: inetOrgPerson",
                "uid: jdoe",
                "cn: John Doe",
                "sn: Doe",
                "givenName: John",
                "mail: john.doe@example.com",
                "telephoneNumber: +1-555-0100",
                "title: Software Engineer",
                "departmentNumber: Engineering"));

            connection.add(new AddRequest(
                "dn: uid=asmith,ou=people,dc=example,dc=com",
                "objectClass: top",
                "objectClass: person",
                "objectClass: organizationalPerson",
                "objectClass: inetOrgPerson",
                "uid: asmith",
                "cn: Alice Smith",
                "sn: Smith",
                "givenName: Alice",
                "mail: alice.smith@example.com",
                "telephoneNumber: +1-555-0101",
                "title: Senior Software Engineer",
                "departmentNumber: Engineering"));

            connection.add(new AddRequest(
                "dn: uid=bjones,ou=people,dc=example,dc=com",
                "objectClass: top",
                "objectClass: person",
                "objectClass: organizationalPerson",
                "objectClass: inetOrgPerson",
                "uid: bjones",
                "cn: Bob Jones",
                "sn: Jones",
                "givenName: Bob",
                "mail: bob.jones@example.com",
                "telephoneNumber: +1-555-0102",
                "title: Product Manager",
                "departmentNumber: Product"));

            System.out.println("    Added 3 user entries");

            // Line 96-100: Search for all entries in the people organizational unit
            System.out.println("\n[4] Searching for all people...");
            SearchRequest searchRequest = new SearchRequest(
                "ou=people,dc=example,dc=com",
                SearchScope.SUB,
                "(objectClass=inetOrgPerson)");

            SearchResult searchResult = connection.search(searchRequest);
            System.out.println("    Found " + searchResult.getEntryCount() + " entries:");

            // Line 106-113: Display all found entries
            for (SearchResultEntry entry : searchResult.getSearchEntries()) {
                System.out.println("\n    DN: " + entry.getDN());
                System.out.println("      CN: " + entry.getAttributeValue("cn"));
                System.out.println("      Email: " + entry.getAttributeValue("mail"));
                System.out.println("      Title: " + entry.getAttributeValue("title"));
                System.out.println("      Department: " + entry.getAttributeValue("departmentNumber"));
                System.out.println("      Phone: " + entry.getAttributeValue("telephoneNumber"));
            }

            // Line 116-128: Search with filter - find users in Engineering department
            System.out.println("\n[5] Searching for Engineering department members...");
            SearchRequest engineeringSearch = new SearchRequest(
                "ou=people,dc=example,dc=com",
                SearchScope.SUB,
                "(departmentNumber=Engineering)",
                "cn", "mail", "title");  // Request specific attributes

            SearchResult engineeringResult = connection.search(engineeringSearch);
            System.out.println("    Found " + engineeringResult.getEntryCount() + " engineers:");

            for (SearchResultEntry entry : engineeringResult.getSearchEntries()) {
                System.out.println("      - " + entry.getAttributeValue("cn") +
                                 " (" + entry.getAttributeValue("title") + ")");
            }

            // Line 131-145: Search by specific user ID
            System.out.println("\n[6] Looking up specific user: uid=jdoe...");
            SearchRequest userSearch = new SearchRequest(
                "ou=people,dc=example,dc=com",
                SearchScope.SUB,
                "(uid=jdoe)");

            SearchResult userResult = connection.search(userSearch);
            if (userResult.getEntryCount() > 0) {
                SearchResultEntry user = userResult.getSearchEntries().get(0);
                System.out.println("    User found:");
                System.out.println("      Full Name: " + user.getAttributeValue("cn"));
                System.out.println("      Email: " + user.getAttributeValue("mail"));
                System.out.println("      First Name: " + user.getAttributeValue("givenName"));
                System.out.println("      Last Name: " + user.getAttributeValue("sn"));
            }

            // Line 148-160: Complex search with AND condition
            System.out.println("\n[7] Complex search: Senior engineers...");
            SearchRequest seniorEngineerSearch = new SearchRequest(
                "ou=people,dc=example,dc=com",
                SearchScope.SUB,
                "(&(departmentNumber=Engineering)(title=Senior*))",
                "cn", "mail", "title");

            SearchResult seniorResult = connection.search(seniorEngineerSearch);
            System.out.println("    Found " + seniorResult.getEntryCount() + " senior engineer(s):");

            for (SearchResultEntry entry : seniorResult.getSearchEntries()) {
                System.out.println("      - " + entry.getAttributeValue("cn"));
            }

            // Line 163-165: Close connection and shutdown server
            System.out.println("\n[8] Cleaning up...");
            connection.close();
            ldapServer.shutDown(true);
            System.out.println("    LDAP connection closed and server stopped");

            System.out.println("\n=== Example completed successfully ===");

        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
