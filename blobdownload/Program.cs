using Azure.Core;
using Azure.Identity;
using Azure.Security.KeyVault.Secrets;
using Azure.Storage.Blobs;
using Azure.Storage.Blobs.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace blobdownload
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Set your Managed Identity Client ID
            string userAssignedClientId = "<your managed identity resource ID>";
            var credential = new DefaultAzureCredential(
                new DefaultAzureCredentialOptions
                {
                    ManagedIdentityClientId = new ResourceIdentifier(userAssignedClientId)
                });

            // Set your key vault uri
            var keyVaultUri = new Uri("<your key vault uri>");
            var secretClient = new SecretClient(keyVaultUri, credential);
            Console.WriteLine(secretClient.VaultUri);

            // Setting your Storage Account ConnStr into Key Vault Secret in portal and recording your secret name.
            var secretName = "<your secret name stored storage account conn str>";
            // Getting your Storage Account ConnStr via Key Vault SDK. Please make sure you have assign your managed identity Key Vault Administrator role in RBAC.
            var storageAccountConnStr = secretClient.GetSecret(secretName).Value.Value;


            // Downloading storage blob
            string containerName = "<your container name>";

            BlobContainerClient container = new BlobContainerClient(storageAccountConnStr, containerName);
            container.CreateIfNotExists();

            foreach (BlobItem blob in container.GetBlobs())
            {
                Console.WriteLine(blob.Name);
                BlobClient blobClient = container.GetBlobClient(blob.Name);
                blobClient.DownloadTo($"D://{blob.Name}");
            }
            Console.ReadKey();
        }
    }
}
